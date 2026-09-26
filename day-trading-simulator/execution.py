from dataclasses import dataclass
import random
from config import SimulationConfig
from models import Order, OrderType, Side

@dataclass
class MarketSnapshot:
    bid: float
    ask: float
    last: float

class ExecutionEngine:
    def __init__(self, config, seed=42):
        self.config = config
        self.rng = random.Random(seed)

    def quote(self, last):
        half = last * self.config.spread_bps / 20000
        return MarketSnapshot(last-half, last+half, last)

    def fill_price(self, side, last):
        q = self.quote(last)
        base = q.ask if side == Side.BUY else q.bid
        slip = base * self.config.slippage_bps / 10000
        return base + slip if side == Side.BUY else base - slip

    def should_trigger(self, order, snapshot):
        if order.order_type == OrderType.MARKET:
            return True
        if order.order_type == OrderType.LIMIT:
            return ((order.side == Side.BUY and snapshot.ask <= order.limit_price) or
                    (order.side == Side.SELL and snapshot.bid >= order.limit_price))
        if order.order_type == OrderType.STOP:
            return ((order.side == Side.BUY and snapshot.last >= order.stop_price) or
                    (order.side == Side.SELL and snapshot.last <= order.stop_price))
        if order.order_type == OrderType.STOP_LIMIT:
            stop_hit = ((order.side == Side.BUY and snapshot.last >= order.stop_price) or
                        (order.side == Side.SELL and snapshot.last <= order.stop_price))
            limit_hit = ((order.side == Side.BUY and snapshot.ask <= order.limit_price) or
                         (order.side == Side.SELL and snapshot.bid >= order.limit_price))
            return stop_hit and limit_hit
        return False

    def fill_quantity(self, remaining, volume):
        if remaining <= 0:
            return 0
        participation_cap = max(1, int(max(volume, 1) * 0.10))
        return min(remaining, participation_cap)
