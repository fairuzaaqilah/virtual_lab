import streamlit as st
import itertools
import math

st.title("🧃 Laboratorium Virtual Kombinasi Buah")

# Daftar buah yang tersedia (bisa kamu sesuaikan)
daftar_buah_tersedia = [
    "Apel", "Jeruk", "Mangga", "Pisang", "Stroberi",
    "Semangka", "Nanas", "Anggur", "Kiwi", "Melon",
    "Blueberry", "Ceri", "Alpukat"
]

# Slider untuk memilih jumlah buah yang ingin dipakai
jumlah_buah = st.slider(
    "Pilih jumlah jenis buah yang ingin digunakan:",
    min_value=1,
    max_value=len(daftar_buah_tersedia),
    value=5
)

# Dropdown dinamis sesuai jumlah_buah yang dipilih
buah_list = []
st.markdown("### Pilih buah:")
for i in range(jumlah_buah):
    buah = st.selectbox(f"Buah ke-{i+1}:", daftar_buah_tersedia, key=f"buah_{i}")
    buah_list.append(buah)

# Hapus duplikat agar kombinasi valid
buah_list = list(dict.fromkeys(buah_list))
n = len(buah_list)

# Input r
r = st.number_input(
    "Jumlah buah yang ingin dicampur (r):",
    min_value=1,
    max_value=n if n > 0 else 1,
    value=2,
    step=1
)

# Validasi dan tampilkan kombinasi
if n >= r and r > 0:
    total_kombinasi = math.comb(n, r)
    hasil_kombinasi = list(itertools.combinations(buah_list, r))

    st.success(f"Jumlah kombinasi (C({n}, {r})) = {total_kombinasi}")

    st.write("### 🔽 Daftar Kombinasi:")
    for i, combo in enumerate(hasil_kombinasi, 1):
        st.write(f"{i}. {', '.join(combo)}")
else:
    st.warning("Jumlah buah (n) harus ≥ r dan r > 0.")
