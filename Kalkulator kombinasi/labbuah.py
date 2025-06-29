import streamlit as st
import itertools
import math

st.title("🧃 Laboratorium Virtual Kombinasi Buah")

# Dictionary emoji buah
emoji_dict = {
    "Apel": "🍎",
    "Jeruk": "🍊",
    "Mangga": "🥭",
    "Pisang": "🍌",
    "Stroberi": "🍓",
    "Semangka": "🍉",
    "Nanas": "🍍",
    "Anggur": "🍇",
    "Kiwi": "🥝",
    "Melon": "🍈",
    "Blueberry": "🫐",
    "Ceri": "🍒",
    "Alpukat": "🥑"
}

# Semua buah tersedia
daftar_buah_tersedia = list(emoji_dict.keys())

# Pilih jumlah buah yang ingin digunakan
jumlah_buah = st.slider("Berapa jenis buah ingin digunakan?", min_value=2, max_value=len(daftar_buah_tersedia), value=5)

# Buat dropdown sebanyak jumlah_buah
st.markdown("### Pilih Buah:")
buah_dipilih = []
for i in range(jumlah_buah):
    buah = st.selectbox(f"Buah ke-{i+1}:", daftar_buah_tersedia, key=f"buah_{i}")
    if buah not in buah_dipilih:
        buah_dipilih.append(buah)

n = len(buah_dipilih)

# Pilih r
r = st.number_input("Jumlah buah yang ingin dicampur (r):", min_value=1, max_value=n, value=2, step=1)

# Fungsi untuk menambahkan emoji
def tambah_emoji(nama):
    emoji = emoji_dict.get(nama, "")
    return f"{emoji} {nama}" if emoji else nama

# Tampilkan hasil kombinasi
if n >= r and r > 0:
    total_kombinasi = math.comb(n, r)
    hasil_kombinasi = list(itertools.combinations(buah_dipilih, r))

    st.success(f"Jumlah kombinasi (C({n}, {r})) = {total_kombinasi}")

    st.write("### 🔽 Daftar Kombinasi:")
    for i, combo in enumerate(hasil_kombinasi, 1):
        emoji_combo = [tambah_emoji(buah) for buah in combo]
        st.write(f"{i}. {', '.join(emoji_combo)}")
else:
    st.warning("Jumlah buah (n) harus ≥ r dan r > 0.")
