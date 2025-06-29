import streamlit as st
import itertools
import math

st.set_page_config(page_title="Laboratorium Virtual Kombinasi Buah", layout="centered")

daftar_buah_tersedia = [
    "Apel", "Jeruk", "Mangga", "Pisang", "Stroberi",
    "Semangka", "Nanas", "Anggur", "Kiwi", "Melon",
    "Blueberry", "Ceri", "Alpukat"
]

# Sidebar menu
menu = st.sidebar.selectbox("Menu", ["Panduan", "Simulasi"])

if menu == "Panduan":
    st.title("📖 Panduan Laboratorium Virtual Kombinasi Buah")

    st.markdown("""
    Selamat datang di laboratorium virtual kombinasi buah!  
    Berikut cara menggunakan aplikasi ini:

    1. **Simulasi**:  
       - Pilih menu *Simulasi* di sidebar.  
       - Gunakan slider untuk memilih jumlah jenis buah (n).  
       - Sistem otomatis memilih n buah pertama dari daftar buah tersedia.  
       - Pilih jumlah buah yang ingin dicampur (r) menggunakan slider.  
       - Klik tombol **Generate Kombinasi** untuk melihat daftar kombinasi buah yang mungkin.  
       
    2. **Catatan**:  
       - Nilai *r* harus kurang dari atau sama dengan *n*.  
       - Kombinasi dihitung berdasarkan rumus matematika C(n, r).  
       - Daftar buah bisa disesuaikan di kode sumber sesuai kebutuhan.  
       
    Selamat mencoba dan bereksperimen dengan kombinasi buah untuk jus favoritmu! 🧃🍓
    """)

elif menu == "Simulasi":
    st.title("🧃 Simulasi Kombinasi Buah")

    # Pilih jumlah buah yang ingin digunakan
    jumlah_buah = st.slider(
        "Pilih jumlah jenis buah yang ingin digunakan (n):",
        min_value=1,
        max_value=len(daftar_buah_tersedia),
        value=5
    )

    # Daftar buah yang dipakai
    buah_list = daftar_buah_tersedia[:jumlah_buah]
    n = len(buah_list)

    st.markdown(f"**Buah yang digunakan:** {', '.join(buah_list)}")

    # Slider untuk memilih r (jumlah buah dalam kombinasi)
    r = st.slider(
        "Jumlah buah yang ingin dicampur (r):",
        min_value=1,
        max_value=n,
        value=2
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
