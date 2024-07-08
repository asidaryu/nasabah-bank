from streamlit_lottie import st_lottie
import streamlit as st
import json

# Menambahkan title dan icon pada page
st.set_page_config(
    page_title="Hasil Prediksi",
    page_icon="♣️"
)

# Menambahkan gambar di sidebar
st.sidebar.markdown(
    '<div style="display: flex; justify-content: center; position: fixed; top: 0; width: 23%; height: 12%; margin-top: 1%;">'
    '<img src="https://i.pinimg.com/564x/af/55/59/af5559f0ac8614f6c1916bb97e6e5a1c.jpg" style="object-fit: cover; width: 75px; height: 75px; border-radius: 50%; overflow: hidden;">'
    '</div>',
    unsafe_allow_html=True
)

# Menambahkan animasi
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
lottie_aku = load_lottiefile ("lottie/data.json")
with st.sidebar:
    st_lottie(
        lottie_aku,
        speed= 1,
        reverse= False,
        loop= True,
        quality= "high",
        height=None,
        width=None,
        key= None,
    )

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
        return "Tidak diperbolehkan berlangganan deposito berjangka"
    elif status_pernikahan == "Lajang":
        return "Boleh berlangganan deposito berjangka"
    elif status_pernikahan == "Cerai":
        if pekerjaan == "Dokter":
            return "Tidak diperbolehkan berlangganan deposito berjangka"
        elif pekerjaan == "Guru":
            return "Boleh berlangganan deposito berjangka"
        elif pekerjaan == "Manajer":
            return "Boleh berlangganan deposito berjangka"
        elif pekerjaan == "Pembantu":
            return "Tidak diperbolehkan berlangganan deposito berjangka"
        elif pekerjaan == "Teknisi":
            return "Boleh berlangganan deposito berjangka"
        elif pekerjaan == "Pengusaha":
            if kredit_macet == "Tidak":
                return "Boleh berlangganan deposito berjangka"
            elif kredit_macet == "Tidak Diketahui":
                return "Boleh berlangganan deposito berjangka"
            elif kredit_macet == "Ya":
                if pendidikan == "Diploma":
                    return "Boleh berlangganan deposito berjangka"
                elif pendidikan == "Kursus Profesional":
                    return "Tidak diperbolehkan berlangganan deposito berjangka"
                elif pendidikan == "Sarjana":
                    return "Tidak diperbolehkan berlangganan deposito berjangka"
                elif pendidikan == "SMA":
                    return "Boleh berlangganan deposito berjangka"
    return "Keputusan tidak dapat ditentukan berdasarkan input yang diberikan"

# Tombol untuk menampilkan hasil
if st.button('Hasil Prediksi'):
    hasil_keputusan = keputusan_berlangganan(status_pernikahan, pekerjaan, kredit_macet, pendidikan)
    st.write(f"### Keputusan: {hasil_keputusan}")


