import pandas as pd
import mysql.connector

# MySQL bağlantısı
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='urun_onerisi'
)

# Veriyi çek
query = "SELECT * FROM urunler"
df = pd.read_sql(query, conn)

conn.close()

print(df.head())  # İlk 5 satırı gör
