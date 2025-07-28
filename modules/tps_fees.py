import pandas as pd
import altair as alt
import os

# Load TPS & fee data
def load_tps_fees(data_path: str = "data/tps_fees_5y_monthly_v2.csv"):
    abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", data_path)
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"Data file not found:{abs_path}，verify that tps_fees_5y_monthly.csv exists in the data/ directory")
    df = pd.read_csv(abs_path)
    df['month'] = pd.to_datetime(df['month'])
    return df

# Add a column for total TPS
def add_total_tps(df: pd.DataFrame):
    df['total_tps'] = df['tps'] / (1 - 0.88)  #Around 12% of the transactions are effective.
    return df

def aggregate_by_quarter(df: pd.DataFrame):
    df_q = df.copy()
    df_q['year'] = df_q['month'].dt.year
    df_q['quarter'] = df_q['month'].dt.quarter
    df_q['quarter_label'] = df_q['year'].astype(str) + 'Q' + df_q['quarter'].astype(str)
    df_q = df_q.groupby('quarter_label', as_index=False)[['tps','total_tps','avg_fee']].mean()
    return df_q

def aggregate_by_year(df: pd.DataFrame):
    df_y = df.copy()
    df_y['year_label'] = df_y['month'].dt.year.astype(str)
    df_y = df_y.groupby('year_label', as_index=False)[['tps','total_tps','avg_fee']].mean()
    return df_y

# Data Visualization
def plot_tps_fees(df: pd.DataFrame, x_col: str, title: str):
    base = alt.Chart(df).encode(x=alt.X(f'{x_col}:O', title=x_col))

   # Left axis: TPS
    line_tps = base.mark_line(point=True, color='blue').encode(
        y=alt.Y('tps:Q', title='TPS'),
        tooltip=[x_col, 'tps', 'avg_fee']
    )

   # Right axis: Avg Fee
    line_fee = base.mark_line(point=True, color='orange').encode(
        y=alt.Y('avg_fee:Q', title='Average Fee (SOL)', axis=alt.Axis(format=".5f")),
        tooltip=[x_col, 'tps', 'avg_fee']
    )

    chart = alt.layer(line_tps, line_fee).resolve_scale(
        y='independent'
    ).properties(
        title=title,
        width=700,
        height=400
    )
    return chart
