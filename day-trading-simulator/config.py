from dataclasses import dataclass

@dataclass(frozen=True)
class SimulationConfig:
    starting_cash: float = 100_000.0
    commission_per_share: float = 0.005
    min_commission: float = 1.00
    spread_bps: float = 2.0
    slippage_bps: float = 3.0
    max_position_pct: float = 0.20
    max_daily_loss_pct: float = 0.02
    leverage: float = 1.0
    pdt_threshold: int = 25_000
    latency_ms: int = 150
