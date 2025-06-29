import streamlit as st
import itertools
import math

st.title("🧃 Simulasi Kombinasi Buah dengan Input Nama Buah + Emoji")

# Mapping buah ke emoji sederhana
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

# Pilih jumlah buah yang ingin digunakan (n)
jumlah_buah = st.slider(
    "Pilih jumlah jenis buah yang ingin digunakan (n):",
    min_value=1,
    max_value=20,
    value=5
)

st.markdown("### Masukkan nama buah unik:")

buah_list = []
nama_buah_valid = True
duplikat_buah = False

# Input nama buah sebanyak jumlah_buah
for i in range(jumlah_buah):
    buah = st.text_input(f"Buah ke-{i+1}:", key=f"buah_{i}")
    buah_list.append(buah.strip())

# Validasi input nama buah tidak boleh kosong dan tidak boleh duplikat
buah_unik = []
for b in buah_list:
    if b != "" and b.lower() not in [x.lower() for x in buah_unik]:
        buah_unik.append(b)

if len([b for b in buah_list if b.strip() == ""]) > 0:
    st.warning("Nama buah tidak boleh kosong semua.")
    nama_buah_valid = False

if len(buah_unik) != len([b for b in buah_list if b.strip() != ""]):
    st.warning("Tidak boleh memasukkan nama buah yang sama.")
    duplikat_buah = True

def dengan_emoji(nama):
    key = nama.lower()
    if key in emoji_buah:
        return f"{emoji_buah[key]} {nama}"
    else:
        return nama

# Jika input valid, tampilkan slider r dengan max = jumlah buah unik yang valid
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
        else:
            st.warning("Jumlah buah (n) harus ≥ r dan r > 0.")
else:
    st.info("Masukkan nama buah unik untuk mengaktifkan kombinasi.")
