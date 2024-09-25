from model import AllIndicators, IndicatorModel

INDICATORS = AllIndicators(
    pi_cycle_top=IndicatorModel("Pi Cycle Top", "pi-cycle-top"),
    nupl=IndicatorModel("Nupl", "nupl"),
    rhodl_ratio=IndicatorModel("Rhodl Ratio", "rhodl-ratio"),
    investor_tool=IndicatorModel("Investor Tool", "investor-tool"),
    puell_multiple=IndicatorModel("Puell Multiple", "puell-multiple"),
    pi_cycle_top_bottom=IndicatorModel("Pi Cycle Top Bottom", "pi-cycle-top-bottom"),
    mvrv_zscore=IndicatorModel("Mvrv Zscore", "mvrv-zscore"),
    rainbow_indicator=IndicatorModel("Rainbow Indicator", "rainbow-indicator"),
    stock_to_flow=IndicatorModel("Stock-To-Flow", "stock-to-flow"),
)
