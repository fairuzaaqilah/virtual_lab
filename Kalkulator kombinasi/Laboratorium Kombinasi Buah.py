import streamlit as st
import itertools
import math

st.set_page_config(page_title="Laboratorium Kombinasi Buah", layout="centered")

# Emoji mapping
emoji_buah = {
    "apel": "🍎",
    "jeruk": "🍊",
    "mangga": "🥭",
    "pisang": "🍌",
    "stroberi": "🍓",
    "semangka": "🍉",
    "nanas": "🍍",
    "anggur": "🍇",
    "kiwi": "🥝",
    "melon": "🍈",
    "blueberry": "🫐",
    "ceri": "🍒",
    "alpukat": "🥑"
}

# Judul halaman
st.title("🍹 Laboratorium Kombinasi Buah")

st.markdown("""
Selamat datang di laboratorium kombinasi buah!  
Di sini kamu bisa bereksperimen membuat kombinasi buah untuk jus favoritmu 🧃
""")

# Tabs utama (Tujuan dipindah jadi yang pertama)
tab1, tab2, tab3 = st.tabs(["🎯 Tujuan Pembelajaran", "📖 Panduan", "🧃 Simulasi"])

# Tab Tujuan Pembelajaran
with tab1:
    st.subheader("🎯 Tujuan Pembelajaran")

    st.markdown("""
    Setelah menyelesaikan pembelajaran ini, siswa diharapkan dapat memahami konsep  kombinasi sederhana.
    """)

# Tab Panduan
with tab2:
    st.subheader("📖 Panduan Laboratorium Virtual Kombinasi Buah")

    st.markdown("""
    ### 🛠️ Cara Menggunakan:
    1. Buka tab **Simulasi**
    2. Pilih jumlah buah yang ingin digunakan (**n**)
    3. Masukkan nama-nama buah (misalnya: Apel, Jeruk, dll)
    4. Pilih berapa banyak buah ingin dicampur (**r**)
    5. Klik **Generate Kombinasi**
    6. Lihat hasil kombinasi

    ### ⚠️ Catatan:
    - Nama buah tidak boleh **kosong** dan **tidak boleh duplikat**
    """)

# Tab Simulasi
with tab3:
    st.subheader("🧃 Simulasi Kombinasi Buah")

    jumlah_buah = st.slider(
        "Pilih jumlah jenis buah yang ingin digunakan (n):",
        min_value=1,
        max_value=20,
        value=5
    )

    st.markdown("### Masukkan nama buah:")

    buah_list = []
    nama_buah_valid = True
    duplikat_buah = False

    for i in range(jumlah_buah):
        buah = st.text_input(f"Buah ke-{i+1}:", key=f"buah_{i}")
        buah_list.append(buah.strip())

    # Validasi input
    buah_unik = []
    for b in buah_list:
        if b != "" and b.lower() not in [x.lower() for x in buah_unik]:
            buah_unik.append(b)

    if len([b for b in buah_list if b.strip() == ""]) > 0:
        st.warning("⚠️ Nama buah tidak boleh kosong.")
