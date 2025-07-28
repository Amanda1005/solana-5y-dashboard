import pandas as pd
from prophet import Prophet

# Prophet forecasts the next n periods
def forecast_trend(df: pd.DataFrame, date_col: str, value_col: str, periods: int = 12, training_months: int = 36):
    if date_col not in df.columns or value_col not in df.columns:
        raise ValueError(f"The dataset is missing required fields: {date_col} or {value_col}")
    
    df_sorted = df.sort_values(date_col)
    # 取最近 training_months 筆資料做預測
    df_recent = df_sorted.tail(training_months)
    df_prophet = df_recent[[date_col, value_col]].rename(columns={date_col: 'ds', value_col: 'y'})
    
    # Prophet 模型
    model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)
    return forecast, df_recent
