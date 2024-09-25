import polars as pl
import streamlit as st

from constants import INDICATORS
from utils import get_metric_for_dashboard, display_indicator

# Set the title of the dashboard
st.set_page_config(layout="wide")
st.title("Dashboard")


# Create a 3x3 grid layout
cols = st.columns(3)

# Panel 1
with cols[0]:
    display_indicator(INDICATORS.pi_cycle_top)

# Panel 2
with cols[1]:
    display_indicator(INDICATORS.nupl)

# Panel 3
with cols[2]:
    display_indicator(INDICATORS.rhodl_ratio)

# Panel 4
with cols[0]:
    display_indicator(INDICATORS.investor_tool)

# Panel 5
with cols[1]:
    display_indicator(INDICATORS.puell_multiple)

# Panel 6
with cols[2]:
    display_indicator(INDICATORS.pi_cycle_top_bottom)

# Panel 7
with cols[0]:
    display_indicator(INDICATORS.mvrv_zscore)

# Panel 8
with cols[1]:
    display_indicator(INDICATORS.rainbow_indicator)

# Panel 9
with cols[2]:
    display_indicator(INDICATORS.stock_to_flow)
