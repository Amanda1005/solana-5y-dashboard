import pandas as pd

def load_representative_projects():
    # 讀取專案清單（用匹配名稱）
    projects = pd.read_csv("data/representative_projects_matched.csv")
    # 讀取 top_contracts 數據
    contracts = pd.read_csv("data/top_contracts_5y_monthly_v2.csv")
import pandas as pd

# 取最新月份 Top 5
def load_representative_projects():
    projects = pd.read_csv("representative_projects_matched.csv")
    contracts = pd.read_csv("top_contracts_5y_monthly_v2.csv")
    contracts['month'] = pd.to_datetime(contracts['month'])

    # 取最新月份資料
    latest_month = contracts['month'].max()
    latest_data = contracts[contracts['month'] == latest_month]

    # 合併，根據 match_name 匹配
    merged = projects.merge(
        latest_data,
        left_on="match_name",
        right_on="contract",
        how="left"
    )

    # 如果缺數據填0
    merged['share_percent'] = merged['share_percent'].fillna(0)

    # 依類型分類，取 Top 5
    defi_top5 = merged[merged['type'].str.contains("DeFi", case=False)].sort_values("share_percent", ascending=False).head(5)
    nft_top5 = merged[merged['type'].str.contains("NFT", case=False)].sort_values("share_percent", ascending=False).head(5)

    return defi_top5, nft_top5, merged


# 取五年趨勢資料（所有月份）
def load_representative_trends():
    projects = pd.read_csv("data/representative_projects_matched.csv")
    contracts = pd.read_csv("data/top_contracts_5y_monthly_v2.csv")
    contracts['month'] = pd.to_datetime(contracts['month'])

    # 合併，包含所有月份數據
    merged = projects.merge(
        contracts,
        left_on="match_name",
        right_on="contract",
        how="left"
    ).fillna(0)

    return merged


# 測試用
if __name__ == "__main__":
    defi_top5, nft_top5, full_data = load_representative_projects()
    print("Top 5 DeFi:\n", defi_top5[['name', 'share_percent']])
    print("Top 5 NFT:\n", nft_top5[['name', 'share_percent']])

    df_trends = load_representative_trends()
    print("Trend data sample:\n", df_trends.head())
