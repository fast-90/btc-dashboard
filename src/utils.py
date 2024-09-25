import io
import os

import polars as pl
import requests
import streamlit as st
from dotenv import load_dotenv

from model import IndicatorModel

load_dotenv()


class MetricNotFoundError(Exception):
    pass


def fetch_metric(metric: str) -> pl.LazyFrame:
    """Fetch a metric as a DataFrame."""

    url = f"https://api.bitcoinmagazinepro.com/metrics/{metric}"
    headers = {"Authorization": f"Bearer {os.getenv("API_KEY")}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        data = response.json()
    except requests.exceptions.RequestException:
        raise MetricNotFoundError(f"Could not fetch data for metric '{metric}'")
    return pl.scan_csv(io.StringIO(data), try_parse_dates=True)


def get_metric_for_dashboard(metric: str) -> pl.DataFrame:
    df = fetch_metric(metric)
    # Discard null and get most recent value
    df = df.drop_nulls().filter(pl.col("Date") == pl.col("Date").max()).drop("", "Date")
    return df.collect().transpose(
        include_header=True, header_name="Metric", column_names=["Value"]
    )


def display_indicator(metric: IndicatorModel) -> None:
    st.header(metric.name)
    st.table(get_metric_for_dashboard(metric.endpoint))
