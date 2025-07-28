import pandas as pd
from prophet import Prophet
import altair as alt

# Prophet forecasts the next n periods
def forecast_trend(df: pd.DataFrame, date_col: str, value_col: str, periods: int = 12, training_months: int = 36):
    if date_col not in df.columns or value_col not in df.columns:
        raise ValueError(f"The dataset is missing required fields:{date_col} or {value_col}")
    
    df_sorted = df.sort_values(date_col)
    # Retrieve data from the most recent training_months period
    df_recent = df_sorted.tail(training_months)
    df_prophet = df_recent[[date_col, value_col]].rename(columns={date_col: 'ds', value_col: 'y'})
    
    model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)
    return forecast, df_recent

# Data Visualization
def plot_forecast(df: pd.DataFrame, forecast: pd.DataFrame, title: str):
    actual = alt.Chart(df).mark_line(color='blue').encode(
        x='ds:T', y='y:Q'
    )
    predicted = alt.Chart(forecast).mark_line(color='orange', strokeDash=[5,5]).encode(
        x='ds:T', y='yhat:Q'
    )
    band = alt.Chart(forecast).mark_area(opacity=0.2, color='orange').encode(
        x='ds:T', y='yhat_lower:Q', y2='yhat_upper:Q'
    )
    return (band + actual + predicted).properties(title=title, width=700, height=400)
