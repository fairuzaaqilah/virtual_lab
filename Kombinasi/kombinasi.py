import streamlit as st
import math
import pandas as pd
import requests
from streamlit_lottie import st_lottie

# Fungsi untuk memuat animasi dari URL
def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# URL animasi Lottie (bebas ganti dengan yang kamu suka)
lottie_outfit = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_sFZsL2.json")

st.set_page_config(page_title="Kalkulator Outfit", layout="centered")
st.title("👕👖 Kalkulator Kombinasi Outfit Siswa")

st.write("""
Seorang siswa memiliki **4 kaos** dan **3 celana**.  
Berapa banyak kombinasi outfit berbeda (1 kaos & 1 celana) yang bisa dibuat?
""")

# Tampilkan animasi jika tersedia
if lottie_outfit:
    col1, col2 = st.columns([1,1])
    with col1:
        st_lottie(lottie_outfit, height=200, key="outfit")
    with col2:
        st.markdown("""
        - Pilih 1 kaos dari 4  
        - Pilih 1 celana dari 3  
        - **Total kombinasi = 4 × 3 = 12**
        """)
else:
    st.info("Animasi tidak bisa dimuat saat ini.")

# Input interaktif
st.header("🔢 Coba Hitung Sendiri!")
kaos = st.number_input("Jumlah kaos", min_value=0, value=4, step=1)
celana = st.number_input("Jumlah celana", min_value=0, va
