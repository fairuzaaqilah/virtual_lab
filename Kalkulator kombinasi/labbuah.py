import streamlit as st
import itertools
import math

st.set_page_config(page_title="Laboratorium Virtual Kombinasi Buah", layout="centered")

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

menu = st.sidebar.selectbox("Menu", ["Panduan", "Simulasi"])

if menu == "Panduan":
    st.title("📖 Panduan Laboratorium Virtual Kombinasi Buah")

    st.markdown("""
    Selamat datang di laboratorium virtual kombinasi buah!  
    Berikut cara menggunakan aplikasi ini:

    1. **Simulasi**:  
       - Pilih menu *Simulasi* di sidebar.  
       - Gunakan slider untuk memilih jumlah jenis buah (n).  
       - Masukkan nama buah unik satu per satu (tidak boleh duplikat dan tidak kosong).  
       - Pilih jumlah buah yang ingin dicampur (r) menggunakan slider.  
       - Klik tombol **Generate Kombinasi** untuk melihat daftar kombinasi buah yang mungkin lengkap dengan emoji.  
       
    2. **Catatan**:  
       - Nilai *r* harus kurang dari atau sama dengan *n*.  
       - Kombinasi dihitung berdasarkan rumus matematika C(n, r).  
       - Daftar buah bisa disesuaikan di kode sumber sesuai kebutuhan.  
       
    Selamat mencoba dan bereksperimen dengan kombinasi buah untuk jus favoritmu! 🧃🍓
    """)

elif menu == "Simulasi":
    st.title("🧃 Simulasi Kombinasi Buah dengan Input Nama Buah + Emoji")

    jumlah_buah = st.slider(
        "Pilih jumlah jenis buah yang ingin digunakan (n):",
        min_value=1,
        max_value=20,
        value=5
    )

    st.markdown("### Masukkan nama buah unik:")

    buah_list = []
    nama_buah_valid = True
    duplikat_buah = False

    for i in range(jumlah_buah):
        buah = st.text_input(f"Buah ke-{i+1}:", key=f"buah_{i}")
        buah_list.append(buah.strip())

    buah_unik = []
    for b in buah_list:
        if b != "" and b.lower() not in [x.lower() for x in buah_unik]:
            buah_unik.append(b)

    if len([b for b in buah_list if b.strip() == ""]) > 0:
        st.warning("Nama buah tidak boleh kosong semua.")
        nama_buah_valid = False
