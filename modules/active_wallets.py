import pandas as pd
import altair as alt

def load_active_wallets(data_path: str = "data/active_wallets_5y_monthly.csv"):
    df = pd.read_csv(data_path)
    df['month'] = pd.to_datetime(df['month'])
    return df

def aggregate_by_quarter(df: pd.DataFrame):
    df_quarter = df.copy()
    df_quarter['year'] = df_quarter['month'].dt.year
    df_quarter['quarter'] = df_quarter['month'].dt.quarter
    df_quarter['quarter_label'] = df_quarter['year'].astype(str) + 'Q' + df_quarter['quarter'].astype(str)
    df_quarter = df_quarter.groupby('quarter_label', as_index=False)['active_wallets'].mean()
    return df_quarter

def aggregate_by_year(df: pd.DataFrame):
    df_year = df.copy()
    df_year['year_label'] = df_year['month'].dt.year.astype(str)
    df_year = df_year.groupby('year_label', as_index=False)['active_wallets'].mean()
    return df_year

def plot_active_wallets(df: pd.DataFrame, x_col: str, title: str):
    chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X(f'{x_col}:O', title=x_col),
        y=alt.Y('active_wallets:Q', title='Active Wallets'),
        tooltip=[x_col, 'active_wallets']
    ).properties(
        title=title,
        width=700,
        height=400
    )
    return chart

