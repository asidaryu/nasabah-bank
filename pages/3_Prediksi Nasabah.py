import streamlit as st

# Menambahkan title dan icon pada page
st.set_page_config(
    page_title="Hasil Prediksi Nasabah",
    page_icon="⏳"
)

# Menambahkan gambar di sidebar
st.sidebar.markdown(
    '<div style="display: flex; justify-content: center; position: fixed; top: 0; width: 23%; height: 12%; margin-top: 1%;">'
    '<img src="https://i.pinimg.com/564x/af/55/59/af5559f0ac8614f6c1916bb97e6e5a1c.jpg" style="object-fit: cover; width: 75px; height: 75px; border-radius: 50%; overflow: hidden;">'
    '</div>',
    unsafe_allow_html=True
)

# Membuat cover pada menu Contact
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://wallpapercave.com/wp/udSKWo6.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    st.markdown(
        """
        <div style="text-align: center; font-size: 30px; font-family: timesnewroman; margin-bottom: 30px; ">Prediksi Keputusan Nasabah dalam Berlangganan Deposito Berjangka</div>
        """,
        unsafe_allow_html=True
    )

    # Pilihan atribut
    status_pernikahan = st.selectbox("Pilih Status Pernikahan:", [""] + ["Menikah", "Lajang", "Cerai"])
    pekerjaan = st.selectbox("Pilih Pekerjaan:", [""] + ["Dokter", "Guru", "Manajer", "Pembantu", "Teknisi", "Pengusaha"])
    kredit_macet = st.selectbox("Pilih Kredit Macet:", [""] + ["Tidak", "Tidak Diketahui", "Ya"])
    pendidikan = st.selectbox("Pilih Pendidikan:", [""] + ["Diploma", "Kursus Profesional", "Sarjana", "SMA"])

    # Logika keputusan
    def keputusan_berlangganan(status_pernikahan, pekerjaan, kredit_macet, pendidikan):
        if status_pernikahan == "Menikah":
            return "Nasabah tidak diperbolehkan berlangganan deposito berjangka"
        elif status_pernikahan == "Lajang":
            return "Nasabah boleh berlangganan deposito berjangka"
        elif status_pernikahan == "Cerai":
            if pekerjaan == "Dokter":
                return "Nasabah tidak diperbolehkan berlangganan deposito berjangka"
            elif pekerjaan == "Guru":
                return "Nasabah boleh berlangganan deposito berjangka"
            elif pekerjaan == "Manajer":
                return "Nasabah boleh berlangganan deposito berjangka"
            elif pekerjaan == "Pembantu":
                return "Nasabah tidak diperbolehkan berlangganan deposito berjangka"
            elif pekerjaan == "Teknisi":
                return "Nasabah boleh berlangganan deposito berjangka"
            elif pekerjaan == "Pengusaha":
                if kredit_macet == "Tidak":
                    return "Nasabah boleh berlangganan deposito berjangka"
                elif kredit_macet == "Tidak Diketahui":
                    return "Nasabah boleh berlangganan deposito berjangka"
                elif kredit_macet == "Ya":
                    if pendidikan == "Diploma":
                        return "Nasabah boleh berlangganan deposito berjangka"
                    elif pendidikan == "Kursus Profesional":
                        return "Nasabah tidak diperbolehkan berlangganan deposito berjangka"
                    elif pendidikan == "Sarjana":
                        return "Nasabah tidak diperbolehkan berlangganan deposito berjangka"
                    elif pendidikan == "SMA":
                        return "Nasabah boleh berlangganan deposito berjangka"
        return "Hasil prediksi tidak dapat ditemukan, mohon masukkan input yang tepat!"

    # Tombol untuk menampilkan hasil
    if st.button('Hasil Prediksi'):
        hasil_keputusan = keputusan_berlangganan(status_pernikahan, pekerjaan, kredit_macet, pendidikan)
        st.write(f"### Keputusan: {hasil_keputusan}")

if __name__ == "__main__":
    main()
