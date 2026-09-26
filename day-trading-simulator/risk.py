from dataclasses import dataclass

@dataclass
class RiskCheck:
    allowed: bool
    message: str

class RiskManager:
    def __init__(self, config):
        self.config = config

    def validate(self, account, symbol, side, quantity, price):
        if quantity <= 0:
            return RiskCheck(False, 'Quantity must be positive.')
        notional = quantity * price
        if side.value == 'buy' and notional > account.buying_power * self.config.leverage:
            return RiskCheck(False, 'Insufficient simulated buying power.')
        current = account.positions.get(symbol)
        current_value = current.market_value if current else 0.0
        if side.value == 'buy' and current_value + notional > account.equity * self.config.max_position_pct:
            return RiskCheck(False, 'Position exceeds concentration limit.')
        daily_loss = account.equity - account.day_start_equity
        if daily_loss < -(account.day_start_equity * self.config.max_daily_loss_pct):
            return RiskCheck(False, 'Daily loss limit reached.')
        return RiskCheck(True, 'Order passes risk checks.')

    def pdt_warning(self, account):
        if account.equity < self.config.pdt_threshold:
            return 'Simulated PDT warning: frequent same-day round trips may trigger a pattern-day-trading restriction in a margin-account model.'
        return 'PDT threshold warning inactive for this simulated account.'
