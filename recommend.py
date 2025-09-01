import pandas as pd
import mysql.connector
from collections import defaultdict

# ---- Ayarlar ----
CSV_PATH = r"C:\Users\pinargokturk\Desktop\recommender-system\data\online_retail_II.csv"
DB_CONFIG = dict(host="localhost", user="root", password="123456", database="urun_onerisi")
UNDESIRED = ['damaged', 'faulty', 'broken', 'smashed']  # filtrelenecek kelimeler


def _load_stock_to_desc():
    """CSV'den StockCode -> Description eşlemesi"""
    df_csv = pd.read_csv(CSV_PATH, dtype={'StockCode': str}, encoding_errors='ignore')
    df_csv = df_csv[['StockCode', 'Description']].dropna(subset=['Description'])
    df_csv['Description'] = df_csv['Description'].astype(str).str.strip()
    df_csv = df_csv[(df_csv['Description'] != '') & (~df_csv['Description'].str.fullmatch(r'\?+'))]
    if UNDESIRED:
        pattern = '|'.join(UNDESIRED)
        df_csv = df_csv[~df_csv['Description'].str.lower().str.contains(pattern, na=False)]
    df_csv = df_csv.drop_duplicates(subset=['StockCode'])
    df_csv['StockCode'] = df_csv['StockCode'].astype(str).str.strip()
    return df_csv.set_index('StockCode')['Description'].to_dict()


def _load_mysql():
    """MySQL'den gerekli verileri çek"""
    conn = mysql.connector.connect(**DB_CONFIG)
    df = pd.read_sql("SELECT CustomerID, StockCode, Quantity FROM urunler", conn)
    conn.close()
    df = df.dropna(subset=['CustomerID', 'StockCode', 'Quantity'])
    df['StockCode'] = df['StockCode'].astype(str).str.strip()
    df = df[df['Quantity'] > 0]  # sadece pozitif miktarlar
    try:
        df['CustomerID'] = df['CustomerID'].astype(int)
    except Exception:
        pass
    return df


def get_recommendations(customer_id: int, top_n: int = 5):
    """User-based basit öneri. customer_id için ['CODE - Description', ...] döner."""
    df_mysql = _load_mysql()
    stock_to_desc = _load_stock_to_desc()

    # Kullanıcı -> ürün seti
    user_items = defaultdict(set)
    for _, row in df_mysql.iterrows():
        user_items[int(row['CustomerID'])].add(row['StockCode'])

    if customer_id not in user_items:
        return []

    target_items = user_items[customer_id]

    # Benzerlik: ortak ürün sayısı
    scores = {}
    for u, items in user_items.items():
        if u == customer_id:
            continue
        scores[u] = len(target_items & items)

    if not scores:
        return []

    # En benzer 5 kullanıcı
    similar_users = sorted(scores, key=scores.get, reverse=True)[:5]

    # Aday ürünler (benzerlerin alıp kullanıcının almadıkları)
    candidates = set()
    for u in similar_users:
        candidates |= (user_items[u] - target_items)

    # Açıklaması olan ve filtrelerden geçen ürünleri topla
    human_readable = []
    for code in candidates:
        desc = stock_to_desc.get(code)
        if desc:
            human_readable.append(f"{code} - {desc}")

    # Sıralama (stabil görünüm için alfabetik) ve ilk N
    human_readable = sorted(human_readable)[:top_n]
    return human_readable
