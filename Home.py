import plotly.express as px
import streamlit as st
import pandas as pd

# set konfigurasi halaman
st.set_page_config(
    page_title="Home",
    page_icon="🏡"
)
# menambahkan gambar profil di sidebar
st.sidebar.markdown(
    '<div style="display: flex; justify-content: center; position: fixed; top: 0; width: 23%; height: 12%; margin-top: 1%;">'
    '<img src="https://i.pinimg.com/564x/af/55/59/af5559f0ac8614f6c1916bb97e6e5a1c.jpg" style="object-fit: cover; width: 75px; height: 75px; border-radius: 50%; overflow: hidden;">'
    '</div>',
    unsafe_allow_html=True
)

# Filter berdasarkan kategori
category = st.sidebar.selectbox('Pilih Kategori', ['Pekerjaan', 'Pernikahan', 'Pendidikan', 'Kredit Macet'])

def main():
    # Menambahkan deskripsi
    st.markdown(
        """
        <div style="text-align: center; font-size: 50px; font-family: timesnewroman; ">Selamat Datang di Bank Kami</div>
        <div style="font-size: 20px; font-family: timesnewroman; margin-top: 10px;">Kami berkomitmen untuk menyediakan layanan perbankan terbaik bagi Anda. Di sini, Anda dapat mengakses berbagai informasi penting terkait akun Anda.</div>
        """,
        unsafe_allow_html=True
    )

    # Menampilkan informasi penting
    st.markdown(
        """
        <div style="font-size: 25px; font-family: timesnewroman; margin-top: 10px;"><b>Informasi Terkini</b></div>
        <ul style="font-size: 16px; font-family: timesnewroman;">
            <li>Peningkatan suku bunga tabungan menjadi 3.5% mulai bulan depan.</li>
            <li>Kami membuka cabang baru di kota Anda, kunjungi kami untuk informasi lebih lanjut.</li>
            <li>Promo kredit rumah dengan bunga rendah hingga akhir tahun.</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

    # Menambahkan grafik sederhana
    st.markdown('<div style="font-size: 25px; font-family: timesnewroman; "><b>Statistik Data Nasabah</b></div>', unsafe_allow_html=True)
    st.caption('Berdasarkan atribut yang digunakan')

    # Data berdasarkan Rice Production Indonesia Tahu 2020-2022
    data = {
        "Pekerjaan": {
            "Kategori": ["Dokter", "Guru", "Manajer", "Pembantu", "Pengusaha", "Teknisi"],
            "Persentase": [3, 13, 9, 6, 10, 9]
        },
        "Pernikahan": {
            "Kategori": ["Cerai", "Lajang", "Menikah"],
            "Persentase": [17, 17, 16]
        },
        "Pendidikan": {
            "Kategori": ["Diploma", "Kursus Profesional", "Sarjana", "SMA"],
            "Persentase": [15, 9, 11, 15]
        },
        "Kredit Macet": {
            "Kategori": ["Tidak", "Tidak Diketahui", "Ya"],
            "Persentase": [6, 18, 26]
        }
    }

    selected_data = data[category]
    df = pd.DataFrame(selected_data)

    fig = px.bar(df, x="Kategori", y="Persentase", title=f"Statistik Data {category}")
    st.plotly_chart(fig)

    # Menambahkan section layanan
    st.markdown(
        """
        <div style="font-size: 25px; font-family: timesnewroman;"><b>Layanan Kami</b></div>
        <ul style="font-size: 16px; font-family: timesnewroman;">
            <li>Tabungan dan Investasi</li>
            <li>Kredit Rumah dan Kendaraan</li>
            <li>Kartu Kredit dengan Berbagai Keuntungan</li>
            <li>Layanan Perbankan Digital</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

    # Menambahkan kontak
    st.markdown(
    """
    <div style="font-size: 25px; font-family: timesnewroman;"><b>Hubungi Kami</b></div>
    <div style="font-size: 16px; font-family: timesnewroman;">
        <div style="display: flex; align-items: center;">
            <img src="https://i.pinimg.com/564x/2b/3f/59/2b3f5903e6ef99075ab2f2fee8c11763.jpg" style="object-fit: cover; width: 30px; height: 30px; border-radius: 50%; margin-right: 10px;">
            <p style="margin-top:15px;">Alamat: 4671 Sugar Camp Road, Owatonna, Minnesota</p>
        </div>
        <div style="display: flex; align-items: center;">
            <img src="https://i.pinimg.com/564x/8d/e5/50/8de5507d6f51f9c8b64d90c175c0b1e5.jpg" style="object-fit: cover; width: 30px; height: 30px; border-radius: 50%; margin-right: 10px;">
            <p style="margin-top:15px;">Telepon: (+62) 89-788-246-125</p>
        </div>
        <div style="display: flex; align-items: center;">
            <img src="https://i.pinimg.com/564x/45/af/cb/45afcb072e032c54b0dfc739e67d25ab.jpg" style="object-fit: cover; width: 30px; height: 30px; border-radius: 50%; margin-right: 10px;">
            <p style="margin-top:15px;">Email: nasabah_bank@gmail.com</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

if __name__ == '__main__':
    main()