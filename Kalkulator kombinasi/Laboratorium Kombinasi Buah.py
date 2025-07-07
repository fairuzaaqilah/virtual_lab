if st.button("Generate Kombinasi"):
    if len(buah_unik) >= r and r > 0:
        total_kombinasi = math.comb(len(buah_unik), r)
        hasil_kombinasi = list(itertools.combinations(buah_unik, r))

        st.success(f"Jumlah kombinasi (C({len(buah_unik)}, {r})) = {total_kombinasi}")

        # Efek animasi 🎈
        st.balloons()
        st.success("🎉 Kombinasi berhasil dibuat!")

        st.write("### 🔽 Daftar Kombinasi:")
        for i, combo in enumerate(hasil_kombinasi, 1):
            combo_emoji = [dengan_emoji(x) for x in combo]
            st.write(f"{i}. {', '.join(combo_emoji)}")
