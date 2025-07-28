import pandas as pd
import altair as alt

def load_transaction_types(data_path: str = "data/transaction_types_5y_monthly_v2.csv"):
    df = pd.read_csv(data_path)
    df['month'] = pd.to_datetime(df['month'])
    return df

def aggregate_by_quarter(df: pd.DataFrame):
    df_quarter = df.copy()
    df_quarter['year'] = df_quarter['month'].dt.year
    df_quarter['quarter'] = df_quarter['month'].dt.quarter
    df_quarter['quarter_label'] = df_quarter['year'].astype(str) + 'Q' + df_quarter['quarter'].astype(str)
    df_quarter = df_quarter.groupby('quarter_label', as_index=False)[['vote', 'transfer', 'nft_swap', 'defi']].mean()
    return df_quarter

def aggregate_by_year(df: pd.DataFrame):
    df_year = df.copy()
    df_year['year_label'] = df_year['month'].dt.year.astype(str)
    df_year = df_year.groupby('year_label', as_index=False)[['vote', 'transfer', 'nft_swap', 'defi']].mean()
    return df_year

def plot_grouped_bar(df: pd.DataFrame, x_col: str, title: str):
    df_melted = df.melt(id_vars=[x_col], value_vars=['vote','transfer','nft_swap','defi'], 
                        var_name='Type', value_name='Percent')
    chart = alt.Chart(df_melted).mark_bar().encode(
        x=alt.X(f'{x_col}:O', title=x_col),
        y=alt.Y('Percent:Q', title='Transaction Share (%)'),
        color=alt.Color('Type:N', title='Transaction Type'),
        column=alt.Column('Type:N', title='Transaction Type'),
        tooltip=[x_col, 'Type', 'Percent']
    ).properties(
        title=title,
        width=150,
        height=400
    )
    return chart


# Data Visualization
def plot_stacked_bar(df: pd.DataFrame, x_col: str, title: str):
    df_melted = df.melt(id_vars=[x_col], value_vars=['vote','transfer','nft_swap','defi'], 
                        var_name='Type', value_name='Percent')
    chart = alt.Chart(df_melted).mark_bar().encode(
        x=alt.X(f'{x_col}:O', title=x_col),
        y=alt.Y('Percent:Q', stack='normalize', title='Transaction Share (%)'),
        color=alt.Color('Type:N', title='Transaction Type'),
        tooltip=[x_col, 'Type', 'Percent']
    ).properties(
        title=title,
        width=700,
        height=400
    )
    return chart


def plot_multi_line(df: pd.DataFrame, x_col: str, title: str):
    df_melted = df.melt(id_vars=[x_col], value_vars=['vote','transfer','nft_swap','defi'], 
                        var_name='Type', value_name='Percent')
    chart = alt.Chart(df_melted).mark_line(point=True).encode(
        x=alt.X(f'{x_col}:O', title=x_col),
        y=alt.Y('Percent:Q', title='Transaction Share (%)'),
        color=alt.Color('Type:N', title='Transaction Type'),
        tooltip=[x_col, 'Type', 'Percent']
    ).properties(
        title=title,
        width=700,
        height=400
    )
    return chart

