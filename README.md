1. Business Value
This dashboard helps investors, protocol developers, and infrastructure teams quickly understand Solana’s key on-chain metrics over the past 5 years, supporting market strategy, product iteration, and resource planning.

2. Pain Points
Fragmented on-chain data: Lack of an integrated view makes it difficult to quickly assess ecosystem activity.
Lack of dynamic observation: No tool simultaneously captures both long-term trends and short-term fluctuations.
Trend forecasting challenges: No model to predict user activity and transaction load, causing delays in resource and strategy planning.

3. Solution
Multi-granularity analysis: Supports annual & quarterly data switching, balancing overall and detailed insights.
Core metrics visualization: Active wallets, TPS, fees, transaction type breakdown, and top contract rankings.
Forecasting model: Uses Prophet to predict 6–12 months of active wallets and TPS, aiding forward-looking planning.
Interactive dashboard: Customizable observation periods for operations, technical teams, and investors.

4. Insights by Module
- Active Wallets
User activity grew steadily from 2020 to 2025, surpassing 6M active wallets in 2025.
After a temporary decline in 2022, growth rebounded strongly from 2024, showing ecosystem recovery.

- TPS & Fees
Effective TPS increased steadily with network usage, exceeding 4,500 by 2025.
Average transaction fees remained within the 0.02–0.06 SOL range, reflecting well-controlled costs.

- Transaction Behavior
DeFi and NFT transactions increased year over year, while Vote transactions declined in share.
Transfer transactions gradually decreased, showing a shift from simple transfers to protocol interactions.

- Top Contracts
From 2020–2025, Vote Program and Token Program consistently ranked top, reflecting stable core infrastructure demand.
Magic Eden, Raydium, and Orca saw significant growth, demonstrating an increasingly diverse ecosystem.

- Forecast (Prophet)
By 2026, active wallets are projected to reach 8–9M, with TPS exceeding 6,000.
Indicates Solana’s strong momentum in high-frequency transactions and user growth.

5. Tech Stack
Data Analysis: Python (Pandas, Prophet, Altair)
Frontend Dashboard: Streamlit
Data Source: Based on Solana public on-chain data (modeled and simulated)




1. 專案價值（Business Value）
本儀表板幫助 投資人、協議開發者與基礎設施團隊，快速掌握 Solana 生態 5 年核心鏈上指標，支援 市場策略、產品迭代與資源規劃。

2. 商業痛點（Pain Points）
鏈上數據零散：缺乏整合視角，難以快速判斷生態活躍
缺少動態觀察：缺乏同時兼顧長期趨勢與短期波動的觀察工具
趨勢預測困難：缺乏能預測活躍度、交易負載的模型，資源與策略規劃滯後

3. 我的解決方案（Solution）
多顆粒度分析：支援年度 & 季度數據切換，兼顧全局與細節觀察
核心指標展示：活躍錢包、TPS、手續費、交易行為結構、熱門合約排名
預測模型：利用 Prophet 模型，預測未來 6–12 個月的活躍錢包與 TPS
交互式儀表板：自訂觀察期間，支援運營、技術、投資多場景決策需求

4. 模組與 Insight（Insights by Module）

- 活躍錢包（Active Wallets）
用戶活躍度自 2020 至 2025 呈 持續增長，2025 年突破 600 萬
2022 年短期回落後，2024 年起明顯回升，顯示生態復甦

- TPS 與手續費
有效 TPS 隨網路使用量提升穩步上升，2025 年突破 4,500
平均手續費保持在 0.02–0.06 SOL 區間，顯示交易成本控制良好

- 交易行為
DeFi 與 NFT 交易占比 逐年上升，Vote 交易比重下降
轉帳類交易逐年減少，顯示用戶偏好從單純轉帳轉向協議互動

- 熱門合約
2020–2025 年 Vote Program 與 Token Program 長期居前，顯示基礎層需求穩定
Magic Eden、Raydium、Orca 等 DeFi/NFT 協議顯著增長，展現應用多元化

- 預測（Prophet）
預測 2026 年活躍錢包將達 800–900 萬，TPS 突破 6,000
預示 Solana 在高頻交易與用戶增長方面仍具強勁動能

5. 技術棧（Tech Stack）
資料分析：Python（Pandas、Prophet、Altair）
前端儀表板：Streamlit
資料來源：基於 Solana 公鏈開放數據（模擬建模）