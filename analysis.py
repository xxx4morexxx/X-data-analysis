import pandas as pd

# CSVファイルリスト（GitHubのdataフォルダにあると仮定）
file_paths = [
    'data/Data-2024-0924.csv',
    'data/Data-2024-1001.csv',
    'data/Data-2024-1008.csv',
    'data/Data-2024-1015.csv',
    'data/Data-2024-1022.csv',
    'data/Data-2024-1029.csv',
    'data/Data-2024-1105.csv',
    'data/Data-2024-1112.csv',
    'data/Data-2024-1126.csv',
    'data/Data-2024-1203.csv',
    'data/Data-2024-1210.csv',
    'data/Data-2024-1217.csv'
]

# 各CSVを読み込んで統合
data_frames = [pd.read_csv(file) for file in file_paths]
combined_data = pd.concat(data_frames, ignore_index=True)

# 投稿数と投稿者数の算出
file_row_counts = {file: len(pd.read_csv(file)) for file in file_paths}
file_account_counts = {file: pd.read_csv(file)['account'].nunique() for file in file_paths}

# データフレーム化
correlation_df = pd.DataFrame({
    "CSVファイルの名前": list(file_row_counts.keys()),
    "投稿数": list(file_row_counts.values()),
    "投稿アカウント数": list(file_account_counts.values())
})

# 平均値の算出
mean_post_count = correlation_df["投稿数"].mean()
mean_account_count = correlation_df["投稿アカウント数"].mean()

print(f"投稿数の平均値: {mean_post_count:.2f}")
print(f"投稿者数の平均値: {mean_account_count:.2f}")

# 相関係数の算出
correlation = correlation_df["投稿数"].corr(correlation_df["投稿アカウント数"])
print(f"投稿数と投稿者数の相関係数: {correlation:.3f}")
