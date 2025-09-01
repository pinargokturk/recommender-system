import pandas as pd
import mysql.connector

# CSV'den sadece gerekli sütunları al
df = pd.read_csv(r'C:/Users/pinargokturk/Desktop/recommender-system/data/online_retail_II.csv')
df = df[['Customer ID', 'StockCode', 'Quantity']]
df = df.rename(columns={'Customer ID':'CustomerID'})

# NaN değerleri doldur
df['CustomerID'] = df['CustomerID'].fillna(0).astype(int)
df['StockCode'] = df['StockCode'].fillna('UNKNOWN')
df['Quantity'] = df['Quantity'].fillna(0).astype(int)

# MySQL bağlantısı
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='urun_onerisi'
)
cursor = conn.cursor()

# Verileri toplu ekleme
data = list(df.itertuples(index=False, name=None))  # tuple listesi
sql = "INSERT INTO urunler (CustomerID, StockCode, Quantity) VALUES (%s, %s, %s)"
cursor.executemany(sql, data)

conn.commit()
cursor.close()
conn.close()

print("Veriler başarıyla MySQL tablosuna aktarıldı!")
