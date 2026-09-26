from datetime import datetime
from uuid import uuid4
from config import SimulationConfig
from execution import ExecutionEngine
from models import Fill, Order, OrderStatus, Side
from portfolio import Portfolio
from risk import RiskManager

class TradingSimulator:
    def __init__(self, config=None):
        self.config = config or SimulationConfig()
        self.portfolio = Portfolio(self.config.starting_cash)
        self.execution = ExecutionEngine(self.config)
        self.risk = RiskManager(self.config)
        self.orders = {}
        self.fills = []
        self.events = []

    def submit_order(self, symbol, side, quantity, order_type, price=None, stop_price=None):
        check_price = price or 0.0
        check = self.risk.validate(self.portfolio.account, symbol, side, quantity, check_price)
        order_id = uuid4().hex[:10]
        order = Order(order_id, symbol, side, quantity, order_type, datetime.utcnow(),
                      limit_price=price if order_type.value in ('limit', 'stop_limit') else None,
                      stop_price=stop_price)
        if not check.allowed:
            order.status = OrderStatus.REJECTED
            order.reason = check.message
        self.orders[order_id] = order
        self.events.append(f'{datetime.utcnow().isoformat()} {order_id}: {order.status.value}')
        return order

    def process_bar(self, symbol, close, volume, timestamp=None):
        snapshot = self.execution.quote(close)
        self.portfolio.mark({symbol: close})
        for order in self.orders.values():
            if order.symbol != symbol or order.status not in (OrderStatus.OPEN, OrderStatus.PARTIALLY_FILLED):
                continue
            if not self.execution.should_trigger(order, snapshot):
                continue
            remaining = order.quantity - order.filled_quantity
            qty = self.execution.fill_quantity(remaining, volume)
            if qty <= 0:
                continue
            price = self.execution.fill_price(order.side, close) if order.order_type == order.order_type.MARKET else close
            commission = max(self.config.min_commission, qty * self.config.commission_per_share)
            fill = Fill(order.id, symbol, order.side, qty, price, timestamp or datetime.utcnow(), commission)
            self.portfolio.apply_fill(fill)
            order.filled_quantity += qty
            order.average_fill_price = price
            order.status = OrderStatus.FILLED if order.filled_quantity == order.quantity else OrderStatus.PARTIALLY_FILLED
            self.fills.append(fill)
        self.portfolio.mark({symbol: close})
