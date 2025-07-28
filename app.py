import streamlit as st
from modules import active_wallets, tps_fees, transaction_types, top_contracts, forecasting

st.set_page_config(page_title="Solana 5-Year Dashboard", layout="wide")
st.title("Solana 5-Year Dashboard")

# ==================== Load global data ====================
df_wallets = active_wallets.load_active_wallets()
df_tps = tps_fees.load_tps_fees()
df_tps = tps_fees.add_total_tps(df_tps)
df_tx = transaction_types.load_transaction_types()
df_contracts = top_contracts.load_top_contracts()

# ==================== Sidebar ====================
st.sidebar.header("Control Panel")
view_type = st.sidebar.radio("Select data granularity", ["Quarterly", "Yearly"])
forecast_months = st.sidebar.slider("Forecast months", min_value=6, max_value=24, value=12)

# ==================== Tabs ====================
tabs = st.tabs([
    "📊 Overview",
    "🔍 Transaction Types",
    "🔥 Top Contracts",
    "📈 Forecasting"
])

# ==================== Overview ====================
with tabs[0]:
    # --- Active Wallets ---
    st.subheader("Active Wallets")
    if view_type == "Quarterly":
        df_wallets_agg = active_wallets.aggregate_by_quarter(df_wallets)
        x_col = 'quarter_label'
        title = 'Quarterly Active Wallets'
    else:
        df_wallets_agg = active_wallets.aggregate_by_year(df_wallets)
        x_col = 'year_label'
        title = 'Yearly Active Wallets'
    chart_wallets = active_wallets.plot_active_wallets(df_wallets_agg, x_col=x_col, title=title)
    st.altair_chart(chart_wallets, use_container_width=True)

    # --- TPS & Transaction Fees ---
    st.subheader("TPS & Transaction Fees")
    tps_type = st.radio("Select display type", ["Effective TPS", "Total TPS"], horizontal=True)
    y_col = 'tps' if tps_type == "Effective TPS" else 'total_tps'

    if view_type == "Quarter":
        df_tps_agg = tps_fees.aggregate_by_quarter(df_tps)
        x_col = 'quarter_label'
        title = f'Quarterly {tps_type} & Avg Fee'
    else:
        df_tps_agg = tps_fees.aggregate_by_year(df_tps)
        x_col = 'year_label'
        title = f'Yearly {tps_type} & Avg Fee'

    df_tps_plot = df_tps_agg[[x_col, y_col, 'avg_fee']].rename(columns={y_col: 'tps'})
    chart_tps = tps_fees.plot_tps_fees(df_tps_plot, x_col=x_col, title=title)
    st.altair_chart(chart_tps, use_container_width=True)

# ==================== Transaction Behavior ====================
with tabs[1]:
    st.subheader("Transaction Behavior Distribution")
    if view_type == "Quarterly":
        df_tx_agg = transaction_types.aggregate_by_quarter(df_tx)
        x_col = 'quarter_label'
        title = 'Quarterly Transaction Types'
    else:
        df_tx_agg = transaction_types.aggregate_by_year(df_tx)
        x_col = 'year_label'
        title = 'Yearly Transaction Types'

    st.markdown("#### Transaction Structure Comparison")
    chart_stacked = transaction_types.plot_stacked_bar(df_tx_agg, x_col=x_col, title=title + " - Stacked Bar")
    st.altair_chart(chart_stacked, use_container_width=True)

    st.markdown("#### Trend Analysis")
    chart_line = transaction_types.plot_multi_line(df_tx_agg, x_col=x_col, title=title + " - Trend Lines")
    st.altair_chart(chart_line, use_container_width=True)

# ==================== Top Contracts ====================
with tabs[2]:
    st.subheader("Annual Top Contracts Ranking")
    df_contracts_agg = top_contracts.aggregate_by_year(df_contracts)
    selected_year = st.selectbox("Select Year", sorted(df_contracts_agg['year'].unique()))
    chart_contracts = top_contracts.plot_top_contracts(df_contracts_agg, year=selected_year)
    st.altair_chart(chart_contracts, use_container_width=True)

# ==================== Forecast ====================
with tabs[3]:
    st.subheader("Active Wallets & TPS Forecast (Prophet)")
    st.markdown("**The model uses data from the past 36 months to forecast the next {} months.**".format(forecast_months))
    
    # --- Active Wallets Forecast ---
    forecast_wallets, df_recent_wallets = forecasting.forecast_trend(
        df_wallets, 'month', 'active_wallets', periods=forecast_months
    )
    chart_wallets_forecast = forecasting.plot_forecast(
        df_recent_wallets.rename(columns={'month':'ds','active_wallets':'y'}), forecast_wallets, 
        "Active Wallets Forecast"
    )
    st.altair_chart(chart_wallets_forecast, use_container_width=True)

    # --- TPS Forecast ---
    forecast_tps, df_recent_tps = forecasting.forecast_trend(
        df_tps, 'month', 'tps', periods=forecast_months
    )
    chart_tps_forecast = forecasting.plot_forecast(
        df_recent_tps.rename(columns={'month':'ds','tps':'y'}), forecast_tps, 
        "TPS Forecast"
    )
    st.altair_chart(chart_tps_forecast, use_container_width=True)

st.markdown("**Data Source:** Simulated data based on Solana public market trends (2020–2025)")

