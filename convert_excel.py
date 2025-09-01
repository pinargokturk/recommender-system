# convert_excel.py
import pandas as pd

# Excel dosyasını oku
excel_dosya = "data/online_retail_II.xlsx"  # Excel dosya adını kontrol et
df = pd.read_excel(excel_dosya, engine="openpyxl")  # openpyxl gerekli

# CSV olarak kaydet
csv_dosya = "data/online_retail_II.csv"
df.to_csv(csv_dosya, index=False)

print(f"Excel dosyası CSV'ye dönüştürüldü: {csv_dosya}")
