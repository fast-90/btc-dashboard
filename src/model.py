from dataclasses import dataclass


@dataclass
class IndicatorModel:
    name: str
    endpoint: str


@dataclass
class AllIndicators:
    pi_cycle_top: IndicatorModel
    nupl: IndicatorModel
    rhodl_ratio: IndicatorModel
    investor_tool: IndicatorModel
    puell_multiple: IndicatorModel
    pi_cycle_top_bottom: IndicatorModel
    mvrv_zscore: IndicatorModel
    rainbow_indicator: IndicatorModel
    stock_to_flow: IndicatorModel
