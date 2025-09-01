# Ürün Öneri Sistemi 🔍

Bu proje, kullanıcıların geçmiş satın alımlarına göre ürün önerileri sunan bir **User-Based Collaborative Filtering** sistemidir.
---

## Proje Amacı

- Kullanıcıların satın alma geçmişine dayalı ürün önerileri üretmek.  
- Staj sürecinde veri bilimi ve yazılım entegrasyonu becerilerini geliştirmek.  

---

## Kullanılan Teknolojiler

- **Python 3.11** – Proje dili  
- **Pandas & Numpy** – Veri işleme ve analiz  
- **MySQL** – Veritabanı (opsiyonel, CSV ile alternatif çalışabilir)  
- **Streamlit** – Web arayüzü  
- **Git & GitHub** – Versiyon kontrolü ve proje paylaşımı  
- **Openpyxl** – Excel/CSV dosyası okuma  
- **SQLAlchemy & mysql-connector-python** – MySQL bağlantısı  
- **User-Based Collaborative Filtering** – Öneri algoritması  

---

## Proje Süreci

1. **Veri Hazırlığı**  
   - `online_retail_II.csv` dosyası işlendi.  
   - Bozuk veya eksik ürün açıklamaları temizlendi.  
   - StockCode ve Description eşlemeleri oluşturuldu.  

2. **Öneri Algoritması**  
   - Basit User-Based Collaborative Filtering kullanıldı.  
   - Kullanıcının geçmiş satın alımları ile benzer kullanıcılar bulundu.  
   - Benzer kullanıcıların aldığı ama hedef kullanıcının almadığı ürünler önerildi.  

3. **Web Arayüzü (Streamlit)**  
   - Streamlit tabanlı web arayüzü
   - Kullanıcı ID girilebilen bir arayüz oluşturuldu.  
   - Önerilen ürünler, StockCode ve açıklaması ile listelendi.  
   - Hem MySQL hem CSV üzerinden çalışabilir hale getirildi.  

4. **Versiyon Kontrol ve Paylaşım**  
   - Proje GitHub’da tutuldu, README, `.gitignore`, `requirements.txt` dosyaları eklendi.  
   - Arkadaşlar ve staj sorumluları projeyi kendi bilgisayarlarında çalıştırabilir.  

---

Projeye katkıda bulunmak isterseniz, pull request açabilir veya issue oluşturabilirsiniz.
