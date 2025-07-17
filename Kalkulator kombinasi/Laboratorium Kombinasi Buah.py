import streamlit as st
import itertools

# Konfigurasi halaman
st.set_page_config(page_title="Laboratorium Kombinasi Buah", layout="centered")

# ===== CSS Background Polos =====
st.markdown("""
    <style>
    .stApp { background-color: #f0f8ff; }
    .block-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem 3rem;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0,0,0,0.05);
    }
    [data-testid="stSidebar"] {
        background-color: #e6f2ff;
    }
    div[data-testid="stTabs"] > div {
        background-color: #e9f4ff;
        border-radius: 8px;
        padding: 5px;
    }
    h1, h2, h3, h4, h5, h6 { color: #2f2f2f; }
    </style>
""", unsafe_allow_html=True)

# Emoji buah
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

# Judul utama
st.title("🍹 Laboratorium Kombinasi Buah")
st.markdown("Selamat datang! Mari bereksperimen membuat kombinasi buah favoritmu untuk jus 🧃")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 Panduan",
    "🎯 Tujuan Pembelajaran",
    "🎓 Pengantar Materi",
    "🧃 Simulasi"
])

# Tab 1 - Panduan
with tab1:
    st.subheader("📖 Panduan Laboratorium Virtual Kombinasi Buah")
    st.markdown("""
    ### 🛠️ Cara Menggunakan:
    1. Buka tab **Tujuan Pembelajaran**.
    2. Baca tab **Pengantar Materi** untuk memahami konsep kombinasi.
    3. Jalankan **Simulasi** untuk membuat kombinasi buah.
    
    ### ⚠️ Catatan:
    - Nama buah harus unik dan tidak boleh kosong.
    """)

# Tab 2 - Tujuan
with tab2:
    st.subheader("🎯 Tujuan Pembelajaran")
    st.markdown("""
    Setelah mengikuti kegiatan ini, kamu diharapkan dapat:
    - Menjelaskan konsep kombinasi
    - Menghitung kombinasi menggunakan rumus
    - Membedakan kombinasi dan permutasi
    - Mengaitkan kombinasi dengan aktivitas sehari-hari
    """)

# Tab 3 - Pengantar Materi
with tab3:
    st.subheader("🎓 Apa Itu Kombinasi?")
    st.markdown("""
    ### 📌 Definisi  
    **Kombinasi** adalah cara memilih sejumlah objek dari sekumpulan objek **tanpa memperhatikan urutan**.

    **Contoh:**  
    Jika kamu punya 3 buah: 🍎 Apel, 🍊 Jeruk, dan 🥭 Mangga, dan memilih 2 buah:
    - Apel & Jeruk  
    - Apel & Mangga  
    - Jeruk & Mangga  

    *Catatan: Apel & Jeruk = Jeruk & Apel → karena urutan tidak penting.*

    ---

    ### 🔢 Rumus Kombinasi

    Kombinasi dari *n* objek yang dipilih *r*:

    $$
    C(n, r) = \\frac{n!}{r!(n - r)!}
    $$

    **Keterangan:**
    - *n* = total objek
    - *r* = objek yang dipilih
    - *!* = faktorial (contoh: 4! = 4 × 3 × 2 × 1 = 24)

    ---

    ### 🧮 Contoh Perhitungan

    Misal ada 5 buah: 🍎 Apel, 🍊 Jeruk, 🥭 Mangga, 🍌 Pisang, 🍓 Stroberi  
    Ingin membuat kombinasi 3 buah:

    $$
    C(5,3) = \\frac{5!}{3!(5-3)!} = \\frac{120}{6 × 2} = \\frac{120}{12} = 10
    $$

    Jadi, ada **10 kombinasi unik** dari 3 buah tersebut.

    ---

    ### 🧃 Penerapan Kombinasi:
    - Campuran jus
    - Menu makanan
    - Pemilihan tim dari siswa

    ---

    ### 🌡️ Siap Bereksperimen?  
    Ayo lanjut ke tab **Simulasi**!
    """)

# Tab 4 - Simulasi
with tab4:
    st.subheader("🧃 Simulasi Kombinasi Buah")
    jumlah_buah = st.slider("Pilih jumlah jenis buah yang ingin digunakan (n):", 1, 20, 5)
    st.markdown("### Masukkan nama buah:")

    buah_list = []
    for i in range(jumlah_buah):
        buah = st.text_input(f"Buah ke-{i+1}:", key=f"buah_{i}")
        buah_list.append(buah.strip())

    # Validasi buah
    buah_unik = []
    for b in buah_list:
        if b != "" and b.lower() not in [x.lower() for x in buah_unik]:
            buah_unik.append(b)

    if len([b for b in buah_list if b.strip() == ""]) > 0:
        st.warning("⚠️ Nama buah tidak boleh kosong.")
    elif len(buah_unik) < len(buah_list):
        st.warning("⚠️ Nama buah tidak boleh duplikat.")
    else:
        r = st.slider("Pilih jumlah buah dalam satu kombinasi (r):", 1, len(buah_unik), min(3, len(buah_unik)))
        if st.button("🔄 Generate Kombinasi"):
            kombinasi = list(itertools.combinations(buah_unik, r))
            st.success(f"Terdapat **{len(kombinasi)}** kombinasi yang mungkin:")
            for i, combo in enumerate(kombinasi, 1):
                combo_with_emoji = [f"{emoji_buah.get(b.lower(), '')} {b}" for b in combo]
                st.write(f"{i}. " + ", ".join(combo_with_emoji))
