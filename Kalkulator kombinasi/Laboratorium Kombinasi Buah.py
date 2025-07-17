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

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 Panduan", 
    "🎯 Tujuan Pembelajaran", 
    "🎓 Pengantar Materi", 
    "🧃 Simulasi"
])

# Tab Panduan
with tab1:
    st.subheader("📖 Panduan Laboratorium Virtual Kombinasi Buah")
    st.markdown("""
    ### 🛠️ Cara Menggunakan:
    1. Buka tab Tujuan Pembelajaran untuk memahami apa yang akan dipelajari.
    2. Lanjut ke tab Pengantar Materi untuk memahami konsep kombinasi.
    3. Klik tab Simulasi untuk bereksperimen.
    4. Pilih jumlah buah (n) dan berapa banyak buah dicampur (r).
    5. Klik Generate Kombinasi untuk melihat hasilnya.

    ### ⚠️ Catatan:
    - Nama buah tidak boleh kosong dan tidak boleh duplikat.
    """)

# Tab Tujuan Pembelajaran
with tab2:
    st.subheader("🎯 Tujuan Pembelajaran")
    st.markdown("""
    Setelah menyelesaikan pembelajaran ini, siswa diharapkan dapat:

    - Menjelaskan pengertian kombinasi dan bahwa urutan tidak berpengaruh.
    - Menuliskan kemungkinan kombinasi dari beberapa benda tanpa rumus.
    - Menggunakan virtual lab kombinasi buah untuk mencoba berbagai kombinasi.
    - Menyelesaikan soal kombinasi dengan rumus yang sesuai.
    - Menjelaskan pengaruh jumlah buah dan yang dipilih terhadap banyaknya kombinasi.
    """)

# Tab Pengantar Materi
with tab3:
    st.subheader("🎓 Apa Itu Kombinasi?")
    
    st.markdown("""
    ### 📌 Definisi  
    Kombinasi adalah cara memilih sejumlah objek dari sekumpulan objek tanpa memperhatikan urutan.

    Contohnya:  
    Jika kamu punya 3 buah: Apel, Jeruk, dan Mangga — dan kamu ingin memilih 2 buah, maka kombinasi yang mungkin adalah:
    - Apel & Jeruk  
    - Apel & Mangga  
    - Jeruk & Mangga
    """)

    st.markdown("""
    ---
    ### 🧮 Rumus Kombinasi

    Kombinasi digunakan saat kita ingin **memilih beberapa objek dari sekumpulan objek** tanpa memperhatikan urutan.

    Rumus kombinasi dinyatakan sebagai:

    \[
    C(n, r) = \\frac{n!}{r!(n - r)!}
    \]
