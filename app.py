import streamlit as st
from recommend import get_recommendations

st.set_page_config(page_title="Ürün Öneri Sistemi", layout="wide")
st.title("Ürün Öneri Sistemi 🔍")

# Kullanıcıdan CustomerID girişi
customer_id = st.number_input("Customer ID giriniz:", min_value=1, step=1)

# CSV kullanımı seçeneği (arkadaşında MySQL yoksa işaretlesin)
use_csv = st.checkbox("MySQL kullanmadan CSV ile çalıştır", value=False)

if st.button("Öneri Getir"):
    try:
        recommended_products = get_recommendations(customer_id, use_csv=use_csv)
        if recommended_products:
            st.subheader("Önerilen Ürünler:")
            for i, product in enumerate(recommended_products, start=1):
                st.write(f"{i}. {product}")
        else:
            st.warning("Bu kullanıcı için öneri bulunamadı.")
    except Exception as e:
        st.error(f"Hata oluştu: {e}")
