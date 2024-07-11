from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import streamlit as st
import pandas as pd
import numpy as np
import graphviz

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

def main():
    st.markdown(
        """
        <div style="font-size: 30px; font-family: timesnewroman; margin-bottom: 30px; ">DATA NASABAH BANK</div>
        """,
        unsafe_allow_html=True
    )
    
    data = {
            "Pekerjaan": ["Pengusaha", "Pembantu", "Pengusaha", "Teknisi", "Guru", "Pengusaha", "Guru", "Manajer", "Teknisi", "Manajer", "Guru", "Pengusaha", "Pengusaha", "Manajer", "Manajer", "Manajer", "Guru", "Pembantu", "Pengusaha", "Manajer", "Guru", "Dokter", "Pembantu", "Guru", "Guru", "Pembantu", "Guru", "Guru", "Pengusaha", "Teknisi", "Teknisi", "Guru", "Pembantu", "Guru", "Manajer", "Guru", "Teknisi", "Guru", "Pembantu", "Dokter", "Teknisi", "Teknisi", "Teknisi", "Teknisi", "Manajer", "Pengusaha", "Dokter", "Manajer", "Pengusaha", "Pengusaha"],
            "Status Pernikahan": ["Menikah", "Menikah", "Cerai", "Menikah", "Cerai", "Lajang", "Lajang", "Lajang", "Menikah", "Cerai", "Menikah", "Cerai", "Menikah", "Menikah", "Lajang", "Menikah", "Cerai", "Lajang", "Lajang", "Lajang", "Cerai", "Menikah", "Menikah", "Menikah", "Cerai", "Lajang", "Lajang", "Menikah", "Cerai", "Lajang", "Cerai", "Menikah", "Lajang", "Lajang", "Lajang", "Menikah", "Cerai", "Menikah", "Cerai", "Cerai", "Menikah", "Cerai", "Menikah", "Lajang", "Cerai", "Cerai", "Menikah", "Lajang", "Cerai", "Lajang"],
            "Pendidikan": ["SMA", "Sarjana", "SMA", "SMA", "SMA", "Kursus Profesional", "SMA", "Sarjana", "Kursus Profesional", "Diploma", "Kursus Profesional", "Diploma", "SMA", "Sarjana", "Diploma", "Diploma", "Sarjana", "Diploma", "SMA", "Diploma", "Diploma", "Kursus Profesional", "Diploma", "Diploma", "SMA", "Sarjana", "Kursus Profesional", "SMA", "Diploma", "Kursus Profesional", "Diploma", "Diploma", "Sarjana", "Diploma", "Sarjana", "SMA", "Sarjana", "Diploma", "Sarjana", "Diploma", "Sarjana", "Sarjana", "SMA", "SMA", "Kursus Profesional", "Kursus Profesional", "SMA", "Kursus Profesional", "SMA", "SMA"],
            "Kredit Macet": ["Tidak", "Tidak Diketahui", "Tidak", "Ya", "Tidak Diketahui", "Ya", "Ya", "Ya", "Ya", "Ya", "Ya", "Tidak Diketahui", "Tidak Diketahui", "Ya", "Ya", "Tidak Diketahui", "Tidak Diketahui", "Tidak", "Ya", "Ya", "Ya", "Ya", "Tidak Diketahui", "Ya", "Ya", "Tidak Diketahui", "Tidak", "Tidak Diketahui", "Tidak Diketahui", "Ya", "Tidak Diketahui", "Tidak Diketahui", "Tidak Diketahui", "Ya", "Ya", "Tidak Diketahui", "Ya", "Tidak Diketahui", "Tidak Diketahui", "Tidak", "Ya", "Tidak Diketahui", "Ya", "Tidak Diketahui", "Ya", "Ya", "Ya", "Tidak", "Ya", "Ya"],
            "Hasil Target": ["Tidak", "Ya", "Tidak", "Ya", "Ya", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Ya", "Ya", "Tidak", "Tidak", "Ya", "Ya", "Ya", "Ya", "Ya", "Tidak", "Tidak", "Tidak", "Ya", "Ya", "Tidak", "Tidak", "Ya", "Tidak", "Tidak", "Ya", "Ya", "Ya", "Ya", "Ya", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Ya", "Ya", "Ya", "Ya", "Tidak", "Tidak", "Ya", "Tidak", "Ya"],
        }
    
    # Menambahkan tabs
    tabel, proses, hasil = st.tabs(["TABEL", "PROSES", "HASIL"])

    with tabel:
        # Buat DataFrame secara manual
        df = pd.DataFrame(data)

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
            height=400,
            fit_columns_on_grid_load=True,
            theme='streamlit',  # Pilih tema: 'streamlit', 'light', 'dark', 'blue', 'fresh', 'material'
            reload_data=True,
            allow_unsafe_jscode=True
        )
    
    with proses:
        df = pd.DataFrame(data)

        def entropy(target_col):
            elements, counts = np.unique(target_col, return_counts=True)
            entropy = -np.sum([(counts[i]/np.sum(counts)) * np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
            return entropy

        def info_gain(data, split_attribute_name, target_name="Hasil Target"):
            total_entropy = entropy(data[target_name])
            vals, counts = np.unique(data[split_attribute_name], return_counts=True)
            weighted_entropy = np.sum([(counts[i]/np.sum(counts)) * entropy(data.where(data[split_attribute_name] == vals[i]).dropna()[target_name]) for i in range(len(vals))])
            information_gain = total_entropy - weighted_entropy
            return information_gain

        # Menghitung entropy dari keseluruhan data
        total_entropy = entropy(df["Hasil Target"])
        st.write("Total Entropy:", total_entropy)

        st.markdown(
        """
        <div style="font-size: 20px; font-family: timesnewroman; color: aqua; margin-bottom: 20px;">Menentukan Value Setiap Attribut</div>
        """,
        unsafe_allow_html=True
        )

        unique_values = {col: df[col].unique().tolist() for col in df.columns}
        unique_df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in unique_values.items()]))
        st.table(unique_df)

        st.markdown(
        """
        <div style="font-size: 20px; font-family: timesnewroman; color: aqua; margin-bottom: 20px;">Menghitung Entropy dan Gain Setiap Attribut</div>
        """,
        unsafe_allow_html=True
        )

        # Menghitung entropy dan gain untuk setiap atribut
        attributes = ["Pekerjaan", "Status Pernikahan", "Pendidikan", "Kredit Macet"]
        entropy_data = []
        gain_data = []

        for attribute in attributes:
            vals, counts = np.unique(df[attribute], return_counts=True)
            entropies = {}
            for val in vals:
                ent_val = entropy(df[df[attribute] == val]["Hasil Target"])
                entropies[val] = ent_val
                entropy_data.append({"Attribute": attribute, "Value": val, "Entropy": ent_val})
            gain = info_gain(df, attribute)
            gain_data.append({"Attribute": attribute, "Gain": gain})

        # Menampilkan nilai entropy dalam bentuk tabel
        entropy_df = pd.DataFrame(entropy_data)
        st.markdown("### Entropy Values")
        st.table(entropy_df)

        # Menampilkan nilai gain dalam bentuk tabel
        gain_df = pd.DataFrame(gain_data)
        st.markdown("### Gain Values")
        st.table(gain_df)

    with hasil:
        st.markdown(
        """
        <div style="font-size: 20px; font-family: timesnewroman;">POHON KEPUTUSAN</div>
        """,
        unsafe_allow_html=True
        )
        # Label Encoding
        df_encoded = df.apply(LabelEncoder().fit_transform)

        X = df_encoded[attributes]
        y = df_encoded["Hasil Target"]
        clf = tree.DecisionTreeClassifier(criterion='entropy')
        clf = clf.fit(X, y)

        # Membuat visualisasi pohon keputusan
        dot_data = tree.export_graphviz(clf, out_file=None,
                                        feature_names=attributes,
                                        class_names=LabelEncoder().fit(df["Hasil Target"]).classes_,
                                        filled=True, rounded=True,
                                        special_characters=True)
        graph = graphviz.Source(dot_data)

        # Tampilkan pohon keputusan di Streamlit
        st.graphviz_chart(dot_data)

if __name__ == "__main__":
    main()
