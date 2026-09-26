from models import Account, Fill, Position, Side

class Portfolio:
    def __init__(self, starting_cash):
        self.account = Account(starting_cash, starting_cash, starting_cash, starting_cash)

    def mark(self, prices):
        total_market_value = 0.0
        for symbol, position in self.account.positions.items():
            if symbol in prices:
                position.last_price = prices[symbol]
                total_market_value += position.market_value
        self.account.equity = self.account.cash + total_market_value
        self.account.buying_power = max(0.0, self.account.equity)

    def apply_fill(self, fill):
        p = self.account.positions.setdefault(fill.symbol, Position(fill.symbol))
        old_qty = p.quantity
        if fill.side == Side.BUY:
            new_qty = old_qty + fill.quantity
            p.average_cost = ((old_qty * p.average_cost) + (fill.quantity * fill.price)) / new_qty
            p.quantity = new_qty
            self.account.cash -= fill.quantity * fill.price + fill.commission
        else:
            if fill.quantity > old_qty:
                raise ValueError('Cannot sell more shares than currently held.')
            pnl = (fill.price - p.average_cost) * fill.quantity
            p.realized_pnl += pnl
            self.account.realized_pnl += pnl
            p.quantity -= fill.quantity
            self.account.cash += fill.quantity * fill.price - fill.commission
            if p.quantity == 0:
                p.average_cost = 0.0
        self.account.fees += fill.commission
