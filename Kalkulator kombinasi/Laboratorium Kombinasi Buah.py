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

# Judul dan pengantar di atas tab
st.title("🍹 Laboratorium Kombinasi Buah")

st.markdown("""
Selamat datang di laboratorium kombinasi buah!  
Di sini kamu bisa bereksperimen membuat kombinasi buah untuk jus favoritmu🧃
""")

# Tabs
tab1, tab2 = st.tabs(["📖 Panduan", "🧃 Simulasi"])

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

                # Animasi balon confetti
                st.balloons()

                # Animasi salju turun pakai HTML + CSS + JS
                snow_html = """
                <style>
                @keyframes snow {
                  0% {transform: translateY(0);}
                  100% {transform: translateY(100vh);}
                }
                .snowflake {
                  position: fixed;
                  top: -10px;
                  z-index: 9999;
                  user-select: none;
                  pointer-events: none;
                  animation-name: snow;
                  animation-timing-function: linear;
                  animation-iteration-count: infinite;
                  animation-duration: 10s;
                  color: white;
                  font-size: 1.5em;
                  text-shadow: 0 0 5px #000;
                }
                .snowflake:nth-child(odd) {
                  animation-duration: 15s;
                  font-size: 1em;
                }
                </style>
                <div class="snowflake" style="left: 10%;">❄️</div>
                <div class="snowflake" style="left: 20%; animation-delay: 2s;">❄️</div>
                <div class="snowflake" style="left: 30%; animation-delay: 4s;">❄️</div>
                <div class="snowflake" style="left: 40%; animation-delay: 6s;">❄️</div>
                <div class="snowflake" style="left: 50%; animation-delay: 8s;">❄️</div>
                <div class="snowflake" style="left: 60%; animation-delay: 10s;">❄️</div>
                <div class="snowflake" style="left: 70%; animation-delay: 12s;">❄️</div>
                <div class="snowflake" style="left: 80%; animation-delay: 14s;">❄️</div>
                <div class="snowflake" style="left: 90%; animation-delay: 16s;">❄️</div>
                """

                st.markdown(snow_html, unsafe_allow_html=True)

            else:
                st.warning("Jumlah buah (n) harus ≥ r dan r > 0.")
    else:
        st.info("Masukkan nama buah terlebih dahulu untuk melanjutkan.")
