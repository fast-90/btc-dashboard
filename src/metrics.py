from typing import Literal


def check_pi_cycle_top(
    ma_111: float, ma_350_double: float
) -> Literal["Overheat", "HODL"]:
    return "Overheat" if ma_111 >= ma_350_double else "HODL"
