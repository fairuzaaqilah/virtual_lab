import streamlit as st
import math
import itertools

st.set_page_config(layout="wide")
st.title("🍹 Laboratorium Kombinasi Buah")

# Nilai tetap untuk kombinasi
n = 6
r = 2

# Daftar buah tetap
buah_list = ["🍎 Apel", "🍌 Pisang", "🍊 Jeruk", "🥭 Mangga", "🍉 Semangka", "🍇 Anggur"]

# Hitung kombinasi teori
def hitung_kombinasi(n, r):
    return math.comb(n, r)

hasil_kombinasi = hitung_kombinasi(n, r)

# Semua kombinasi seharusnya
kombinasi_teori = list(itertools.combinations(sorted(buah_list), r))

# Inisialisasi state
if "kombinasi_buah" not in st.session_state:
    st.session_state.kombinasi_buah = []

# Kolom interaktif
col1, col2 = st.columns(2)

with col1:
    pilihan = st.multiselect(f"Pilih {r} buah berbeda:", buah_list, key="pilih_buah")

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
            st.success("🎉 Kamu berhasil menemukan semua kombinasi!")
    else:
        st.info("Belum ada kombinasi ditambahkan.")

# Tampilkan kombinasi teori
st.divider()
st.markdown("### 📋 Semua Kombinasi yang Mungkin:")
with st.expander("Klik untuk melihat semua kombinasi"):
    for idx, k in enumerate(kombinasi_teori, start=1):
        cek = "✅" if k in st.session_state.kombinasi_buah else "⬜"
        st.write(f"{cek} {idx}. {' + '.join(k)}")
