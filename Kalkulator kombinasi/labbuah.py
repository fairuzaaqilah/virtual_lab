import streamlit as st
import itertools
import math

st.title("🧃 Laboratorium Virtual Kombinasi Buah")

daftar_buah_tersedia = [
    "Apel", "Jeruk", "Mangga", "Pisang", "Stroberi",
    "Semangka", "Nanas", "Anggur", "Kiwi", "Melon",
    "Blueberry", "Ceri", "Alpukat"
]

# Pilih jumlah buah yang ingin digunakan
jumlah_buah = st.slider(
    "Pilih jumlah jenis buah yang ingin digunakan:",
    min_value=1,
    max_value=len(daftar_buah_tersedia),
    value=5
)

# Daftar buah yang dipakai
buah_list = daftar_buah_tersedia[:jumlah_buah]
n = len(buah_list)

st.markdown(f"**Buah yang digunakan:** {', '.join(buah_list)}")

# Input r
r = st.number_input(
    "Jumlah buah yang ingin dicampur (r):",
    min_value=1,
    max_value=n,
    value=2,
    step=1
)

if st.button("Generate Kombinasi"):
    if n >= r and r > 0:
        total_kombinasi = math.comb(n, r)
        hasil_kombinasi = list(itertools.combinations(buah_list, r))

        st.success(f"Jumlah kombinasi (C({n}, {r})) = {total_kombinasi}")

        st.write("### 🔽 Daftar Kombinasi:")
        for i, combo in enumerate(hasil_kombinasi, 1):
            st.write(f"{i}. {', '.join(combo)}")
    else:
        st.warning("Jumlah buah (n) harus ≥ r dan r > 0.")
