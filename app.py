import streamlit as st
from recommend import get_recommendations, _load_mysql

st.set_page_config(page_title="Ürün Öneri Sistemi", layout="wide")
st.title("Ürün Öneri Sistemi 🔍")

# Kullanıcıdan CustomerID girişi
customer_id = st.number_input("Customer ID giriniz:", min_value=1, step=1)

if st.button("Öneri Getir"):
    try:
        recommended_products = get_recommendations(customer_id)
        if recommended_products:
            st.subheader("Önerilen Ürünler:")
            for i, product in enumerate(recommended_products, start=1):
                st.write(f"{i}. {product}")
        else:
            st.warning("Bu kullanıcı için öneri bulunamadı.")
    except Exception as e:
        st.error(f"Hata oluştu: {e}")

# 🔹 Ekstra: Mevcut CustomerID'leri göster
if st.button("Mevcut CustomerID'leri Göster"):
    try:
        df = _load_mysql()
        customer_list = df['CustomerID'].drop_duplicates().tolist()
        st.write("Mevcut CustomerID'ler (ilk 30):", customer_list[:30])
    except Exception as e:
        st.error(f"CustomerID listesi alınamadı: {e}")
