import streamlit as st
import math
import itertools

st.set_page_config(layout="wide")
st.title("🍹 Laboratorium Kombinasi Buah")

st.markdown("### 🔢 Masukkan nilai untuk kombinasi")
n = st.number_input("Jumlah buah tersedia (n)", min_value=2, max_value=20, value=6)
r = st.number_input("Jumlah buah yang dipilih (r)", min_value=1, max_value=int(n), value=2)

# Hitung kombinasi nCr
def hitung_kombinasi(n, r):
    return math.comb(n, r)

hasil_kombinasi = hitung_kombinasi(n, r)

st.markdown(f"""
### 📘 Rumus Kombinasi  
\[
C(n, r) = \\frac{{n!}}{{r!(n-r)!}} = C({n}, {r}) = {hasil_kombinasi}
\]
""")

st.divider()

# Daftar buah disesuaikan dengan n
buah_semua = ["🍎 Apel", "🍌 Pisang", "🍊 Jeruk", "🥭 Mangga", "🍉 Semangka", "🍇 Anggur",
              "🍍 Nanas", "🍓 Stroberi", "🥝 Kiwi", "🍑 Persik", "🍒 Ceri", "🍏 Apel Hijau",
              "🍈 Melon", "🫐 Blueberry", "🥥 Kelapa", "🍋 Lemon", "🍐 Pir", "🍅 Tomat", "🍠 Ubi", "🍆 Terong"]

buah_list = buah_semua[:int(n)]

st.markdown("### 🧃 Pilih buah untuk membuat kombinasi")

if "kombinasi_buah" not in st.session_state:
    st.session_state.kombinasi_buah = []

col1, col2 = st.columns(2)

with col1:
    pilihan = st.multiselect(f"Pilih {r} buah berbeda:", buah_list)

    if st.button("➕ Tambahkan Kombinasi"):
        if len(pilihan) != r:
            st.warning(f"Pilih tepat {r} buah.")
        else:
            kombinasi = tuple(sorted(pilihan))
            if kombinasi not in st.session_state.kombinasi_buah:
                st.session_state.kombinasi_buah.append(kombinasi)
                st.success("Kombinasi berhasil ditambahkan.")
            else:
                st.info("Kombinasi ini sudah ada.")

    if st.button("🔁 Reset Kombinasi"):
        st.session_state.kombinasi_buah = []

with col2:
    st.subheader("🍹 Kombinasi yang Kamu Buat:")
    if st.session_state.kombinasi_buah:
        for i, k in enumerate(st.session_state.kombinasi_buah, 1):
            st.write(f"{i}. {' + '.join(k)}")
        st.info(f"Total: {len(st.session_state.kombinasi_buah)} kombinasi")
        if len(st.session_state.kombinasi_buah) == hasil_kombinasi:
            st.balloons()
            st.success("Kamu berhasil membuat semua kombinasi!")
    else:
        st.info("Belum ada kombinasi ditambahkan.")
