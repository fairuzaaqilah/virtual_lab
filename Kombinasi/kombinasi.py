import streamlit as st
import math
import requests
from streamlit_lottie import st_lottie

# Fungsi untuk load animasi Lottie
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Muat animasi pakaian
lottie_outfit = load_lottie_url("https://assets10.lottiefiles.com/datafiles/5K6XhetK3CPQjrn/data.json")  # contoh animasi

st.set_page_config(page_title="Kalkulator Outfit Interaktif", layout="centered")
st.title("🎽 Kalkulator Outfit Interaktif")

st.write("""
Seorang siswa memiliki **4 kaos** dan **3 celana**.
Berapa banyak cara dia bisa memilih **1 kaos** dan **1 celana** (kombinasi outfit)?
""")

# Animasi di samping penjelasan
if lottie_outfit:
    col1, col2 = st.columns([1,1])
    with col1:
        st_lottie(lottie_outfit, height=200, key="outfit")
    with col2:
        st.write("""
1. Pilih **1 kaos** dari 4  
2. Pilih **1 celana** dari 3  

Total kombinasi = 4 × 3 = **12** cara
""")
else:
    st.write("🤷‍♂️ Animasi tidak tersedia saat ini.")

# Kalkulator interaktif
st.header("🔢 Coba Kalkulasi Sendiri!")
kaos = st.number_input("Jumlah kaos (n)", min_value=0, step=1, value=4)
celana = st.number_input("Jumlah celana (r)", min_value=0, step=1, value=3)

if st.button("Hitung kombinasi"):
    total = kaos * celana
    st.success(f"Ada **{total}** kombinasi berbeda (kaos × celana).")

    # Tampilkan tabel kombinasi
    import pandas as pd
    df = pd.DataFrame([
        {"Kaos": f"Kaos {i+1}", "Celana": f"Celana {j+1}"}
        for i in range(kaos) for j in range(celana)
    ])
    st.dataframe(df, use_container_width=True)

st.write("---")
st.write("Powered by Streamlit 💡")
