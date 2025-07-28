import pandas as pd
import altair as alt

# Load top contracts data
def load_top_contracts(data_path: str = "data/top_contracts_5y_monthly_v2.csv"):
    df = pd.read_csv(data_path)
    df['month'] = pd.to_datetime(df['month'])
    return df

# ggregate to yearly Top 10 contracts
def aggregate_by_year(df: pd.DataFrame):
    df_year = df.copy()
    df_year['year'] = df_year['month'].dt.year
    df_year = df_year.groupby(['year', 'contract'], as_index=False)['share_percent'].mean()
    
    # Top 10 every year
    top_contracts = []
    for year in df_year['year'].unique():
        top10 = df_year[df_year['year'] == year].sort_values('share_percent', ascending=False).head(10)
        top_contracts.append(top10)
    df_top10 = pd.concat(top_contracts)
    df_top10['year'] = df_top10['year'].astype(str)
    return df_top10

# # Data Visualization
def plot_top_contracts(df: pd.DataFrame, year: str):
    df_selected = df[df['year'] == year].sort_values('share_percent', ascending=False)
    chart = alt.Chart(df_selected).mark_bar().encode(
        x=alt.X('share_percent:Q', title='Share (%)'),
        y=alt.Y('contract:N', sort='-x', title='Contract'),
        tooltip=['contract','share_percent']
    ).properties(
        title=f'Top 10 Contracts in {year}',
        width=700,
        height=400
    )
    return chart
