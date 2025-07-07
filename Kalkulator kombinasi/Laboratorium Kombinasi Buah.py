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

# Tabs utama
tab1, tab2, tab3 = st.tabs(["📖 Panduan", "🧃 Simulasi", "🎯 Tujuan Pembelajaran"])

# Tab Panduan
with tab1:
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
with tab2:
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
        nama_buah_valid = False

    if len(buah_unik) != len([b for b in buah_list if b.strip() != ""]):
        st.warning("⚠️ Tidak boleh memasukkan nama buah yang sama.")
        duplikat_buah = True

    def dengan_emoji(nama):
        key = nama.lower()
        return f"{emoji_buah[key]} {nama}" if key in emoji_buah else nama

    if nama_buah_valid and not duplikat_buah and len(buah_unik) > 0:
        r = st.slider(
            "Jumlah buah yang ingin dicampur (r):",
            min_value=1,
            max_value=len(buah_unik),
            value=2
        )

        if st.button("Generate Kombinasi"):
            if len(buah_unik) >= r and r > 0:
                total_kombinasi = math.comb(len(buah_unik), r)
                hasil_kombinasi = list(itertools.combinations(buah_unik, r))

                st.success(f"Jumlah kombinasi (C({len(buah_unik)}, {r})) = {total_kombinasi}")

                st.write("### 🔽 Daftar Kombinasi:")
                for i, combo in enumerate(hasil_kombinasi, 1):
                    combo_emoji = [dengan_emoji(x) for x in combo]
                    st.write(f"{i}. {', '.join(combo_emoji)}")

                st.balloons()
            else:
                st.warning("Jumlah buah (n) harus ≥ r dan r > 0.")
    else:
        st.info("Masukkan nama buah terlebih dahulu untuk melanjutkan.")

# Tab Tujuan Pembelajaran
with tab3:
    st.subheader("🎯 Tujuan Pembelajaran")

    st.markdown("""
    Setelah menyelesaikan aktivitas ini, siswa diharapkan dapat:
    
    - Memahami konsep dasar **kombinasi** dalam matematika
    - Menentukan banyaknya cara memilih objek dari suatu kumpulan tanpa memperhatikan urutan
    - Menerapkan konsep kombinasi dalam situasi nyata, seperti mencampur buah
    - Menganalisis perubahan jumlah kombinasi saat nilai **n** (jumlah buah) atau **r** (jumlah campuran) diubah
    """)
