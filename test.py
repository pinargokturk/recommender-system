import pandas as pd

df = pd.read_csv('C:/Users/pinargokturk/Desktop/recommender-system/data/online_retail_II.csv')
max_len = df['StockCode'].str.len().max()
print(max_len)
