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

    **Keterangan:**
    - `n` = jumlah total objek (misalnya jenis buah)
    - `r` = jumlah objek yang dipilih
    - `!` = faktorial, yaitu hasil perkalian dari bilangan tersebut dengan semua bilangan positif di bawahnya  
      (contoh: \\( 4! = 4 \\times 3 \\times 2 \\times 1 = 24 \\))
    """)

    st.markdown("""
    ---
    ### 📘 Contoh Perhitungan Kombinasi

    Misalnya kamu memiliki **5 jenis buah**:  
    🍎 Apel, 🍊 Jeruk, 🥭 Mangga, 🍌 Pisang, 🍓 Stroberi  

    Lalu kamu ingin membuat kombinasi **3 buah untuk jus**.

    Maka:

    \[
    C(5, 3) = \\frac{5!}{3!(5 - 3)!} = \\frac{5 \\times 4 \\times 3 \\times 2 \\times 1}{3 \\times 2 \\times 1 \\times 2 \\times 1} = \\frac{120}{6 \\times 2} = \\frac{120}{12} = 10
    \]

    Jadi, terdapat **10 kombinasi unik** dari 3 buah yang bisa kamu buat dari 5 jenis buah.
    """)

    st.markdown("""
    ---
    ### 🧃 Penerapan dalam Kehidupan Sehari-hari
    - Membuat campuran jus dari beberapa jenis buah  
    - Menyusun menu makanan dari berbagai pilihan  
    - Memilih tim dari sekelompok siswa

    ---
    ### 🌡️ Siap Bereksperimen?  
    Silakan lanjut ke tab Simulasi untuk mencoba membuat berbagai kombinasi buah menggunakan Laboratorium Virtual 🍹
    """)

# Tab Simulasi
with tab4:
    st.subheader("🧃 Simulasi Kombinasi Buah")

    jumlah_buah = st.slider(
        "Pilih jumlah jenis buah yang ingin digunakan (n):",
        min_value=1,
        max_value=20,
        value=5
    )

    st.markdown("### Masukkan nama buah:")

    buah_list = []
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
    elif len(buah_unik) < len(buah_list):
        st.warning("⚠️ Nama buah tidak boleh duplikat.")
    else:
        r = st.slider(
            "Pilih berapa buah yang ingin dicampur dalam satu kombinasi (r):",
            min_value=1,
            max_value=len(buah_unik),
            value=min(3, len(buah_unik))
        )

        if st.button("🔄 Generate Kombinasi"):
            kombinasi = list(itertools.combinations(buah_unik, r))
            st.success(f"Terdapat {len(kombinasi)} kombinasi yang mungkin:")

            for i, combo in enumerate(kombinasi, 1):
                combo_with_emoji = [f"{emoji_buah.get(b.lower(), '')} {b}" for b in combo]
                st.write(f"{i}. " + ", ".join(combo_with_emoji))
