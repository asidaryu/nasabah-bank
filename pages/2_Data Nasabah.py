import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

# Set konfigurasi halaman
st.set_page_config(
    page_title="Data Nasabah",
    page_icon="📖"
)

# menambahkan gambar profil di sidebar
st.sidebar.markdown(
    '<div style="display: flex; justify-content: center; position: fixed; top: 0; width: 23%; height: 12%; margin-top: 1%;">'
    '<img src="https://i.pinimg.com/564x/af/55/59/af5559f0ac8614f6c1916bb97e6e5a1c.jpg" style="object-fit: cover; width: 75px; height: 75px; border-radius: 50%; overflow: hidden;">'
    '</div>',
    unsafe_allow_html=True
)

# Data nasabah bank
data = {
    "Pekerjaan": ["Pengusaha", "Pembantu", "Pengusaha", "Teknisi", "Guru", "Pengusaha", "Guru", "Manajer", "Teknisi", "Manajer", "Guru", "Pengusaha", "Pengusaha", "Manajer", "Manajer", "Manajer", "Guru", "Pembantu", "Pengusaha", "Manajer", "Guru", "Dokter", "Pembantu", "Guru", "Guru", "Pembantu", "Guru", "Guru", "Pengusaha", "Teknisi", "Teknisi", "Guru", "Pembantu", "Guru", "Manajer", "Guru", "Teknisi", "Guru", "Pembantu", "Dokter", "Teknisi", "Teknisi", "Teknisi", "Teknisi", "Manajer", "Pengusaha", "Dokter", "Manajer", "Pengusaha", "Pengusaha"],
    "Status Pernikahan": ["Menikah", "Menikah", "Cerai", "Menikah", "Cerai", "Lajang", "Lajang", "Lajang", "Menikah", "Cerai", "Menikah", "Cerai", "Menikah", "Menikah", "Lajang", "Menikah", "Cerai", "Lajang", "Lajang", "Lajang", "Cerai", "Menikah", "Menikah", "Menikah", "Cerai", "Lajang", "Lajang", "Menikah", "Cerai", "Lajang", "Cerai", "Menikah", "Lajang", "Lajang", "Lajang", "Menikah", "Cerai", "Menikah", "Cerai", "Cerai", "Menikah", "Cerai", "Menikah", "Lajang", "Cerai", "Cerai", "Menikah", "Lajang", "Cerai", "Lajang"],
    "Pendidikan": ["SMA", "Sarjana", "SMA", "SMA", "SMA", "Kursus Profesional", "SMA", "Sarjana", "Kursus Profesional", "Diploma", "Kursus Profesional", "Diploma", "SMA", "Sarjana", "Diploma", "Diploma", "Sarjana", "Diploma", "SMA", "Diploma", "Diploma", "Kursus Profesional", "Diploma", "Diploma", "SMA", "Sarjana", "Kursus Profesional", "SMA", "Diploma", "Kursus Profesional", "Diploma", "Diploma", "Sarjana", "Diploma", "Sarjana", "SMA", "Sarjana", "Diploma", "Sarjana", "Diploma", "Sarjana", "Sarjana", "SMA", "SMA", "Kursus Profesional", "Kursus Profesional", "SMA", "Kursus Profesional", "SMA", "SMA"],
    "Kredit Macet": ["Tidak", "Tidak Diketahui", "Tidak", "Ya", "Tidak Diketahui", "Ya", "Ya", "Ya", "Ya", "Ya", "Ya", "Tidak Diketahui", "Tidak Diketahui", "Ya", "Ya", "Tidak Diketahui", "Tidak Diketahui", "Tidak", "Ya", "Ya", "Ya", "Ya", "Tidak Diketahui", "Ya", "Ya", "Tidak Diketahui", "Tidak", "Tidak Diketahui", "Tidak Diketahui", "Ya", "Tidak Diketahui", "Tidak Diketahui", "Tidak Diketahui", "Ya", "Ya", "Tidak Diketahui", "Ya", "Tidak Diketahui", "Tidak Diketahui", "Tidak", "Ya", "Tidak Diketahui", "Ya", "Tidak Diketahui", "Ya", "Ya", "Ya", "Tidak", "Ya", "Ya"],
    "Hasil Target": ["Tidak", "Ya", "Tidak", "Ya", "Ya", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Ya", "Ya", "Tidak", "Tidak", "Ya", "Ya", "Ya", "Ya", "Ya", "Tidak", "Tidak", "Tidak", "Ya", "Ya", "Tidak", "Tidak", "Ya", "Tidak", "Tidak", "Ya", "Ya", "Ya", "Ya", "Ya", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Ya", "Ya", "Ya", "Ya", "Tidak", "Tidak", "Ya", "Tidak", "Ya"],
}

# Buat DataFrame secara manual
df = pd.DataFrame(data)

# Menampilkan data nasabah dengan AgGrid
st.write("## Data Nasabah Bank")

# Membuat konfigurasi grid
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True)  # Mengaktifkan pagination
gb.configure_side_bar()  # Mengaktifkan sidebar
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)

# Mengatur agar kolom dapat diklik
cellstyle_jscode = JsCode("""
function(params) {
    if (params.value.includes('Ya')) {
        return {
            'color': 'white',
            'backgroundColor': 'green'
        }
    } else if (params.value.includes('Tidak')) {
        return {
            'color': 'white',
            'backgroundColor': 'red'
        }
    }
    return null;
}
""")

gb.configure_column("Hasil Target", cellStyle=cellstyle_jscode)

gridOptions = gb.build()

# Menampilkan tabel interaktif
grid_response = AgGrid(
    df,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    update_mode='MODEL_CHANGED',
    height=450,
    fit_columns_on_grid_load=True,
    theme='streamlit',  # Pilih tema: 'streamlit', 'light', 'dark', 'blue', 'fresh', 'material'
    reload_data=True,
    allow_unsafe_jscode=True
)

# Menampilkan data yang dipilih
selected = grid_response['selected_rows']
if selected:
    st.write("### Data Terpilih")
    st.write(selected)
