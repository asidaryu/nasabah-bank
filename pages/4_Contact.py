import pyplot as plt
import plotly.express as px
import streamlit as st
import pandas as pd

# Menambahkan title dan icon pada page
st.set_page_config(
    page_title="Shopping Trends",
    page_icon="🛍️"
)

# Menambahkan gambar di sidebar
st.sidebar.markdown(
    '<div style="display: flex; justify-content: center; position: fixed; top: 0; width: 23%; height: 12%; margin-top: 1%;">'
    '<img src="https://i.pinimg.com/564x/31/56/7a/31567a2aea11c60f3792b2f9d09d1dde.jpg" style="object-fit: cover; width: 75px; height: 75px; border-radius: 50%; overflow: hidden;">'
    '</div>',
    unsafe_allow_html=True
)

# Filter berdasarkan kategori
category = st.sidebar.selectbox('Pilih Category', ['Clothing', 'Footwear', 'Accessories'])

# Filter berdasarkan ukuran
size = st.sidebar.radio(
    "Pilih Size:",
    ('S', 'M', 'L', 'XL')
)

# Judul pada page Data
st.markdown(
    '<div style="font-size: 40px; font-family: timesnewroman; margin-bottom: 50px;">Shopping Trends</div>',
    unsafe_allow_html=True
)
st.write('Gender: Male')

# Data berdasarkan Pendidikan Tertinggi Yang Ditamatkan dan Tahunnya
data = {
     "Item Purchased": ["Blouse", "Sweater", "Jeans", "Sandals", "Sneakers", "Shirt", "Coat", "Handbag"],
     "Category Clothing": ["Blouse", "Sweater", "Jeans", "Shirt", "Short", "Dress", "Dress", "Pants"],
     "Category Footwear": ["Sandals", "Sneakers", "Boots", "Shoes", "Flat Shoes", "Ballet Flats", "Galoshes", "Oxfords"],
     "Category Accessories": ["Handbag", "Sunglasses", "Jewelry", "Scarf", "Hat", "Backpack", "Belt", "Gloves"],
     "Purchase Amount (USD)": [53, 64, 73, 90, 49, 20, 85, 34],
     "Purchase Amount (USD) Size S": [73, 36, 45, 21, 94, 43, 32, 73],
     "Purchase Amount (USD) Size M": [90, 81, 69, 94, 36, 91, 95, 92],
     "Purchase Amount (USD) Size L": [53, 53, 43, 79, 46, 53, 41, 100],
     "Purchase Amount (USD) Size XL": [38, 21, 59, 73, 72, 83, 67, 40],
}
# Menambahkan tabs
lingkaran, batang, tabel = st.tabs(["GRAFIK LINGKARAN", "GRAFIK BATANG", "TABEL"])

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c2f0c2', '#ff6666']

with lingkaran:
    # Data
    labels = data[f"Category {category}"]
    sizes = data[f"Purchase Amount (USD) Size {size}"]

    # Explode untuk bagian yang ditekankan
    explode = (0, 0, 0, 0, 0.1, 0, 0.1, 0.2)

    fig1, ax1 = plt.subplots()

    # Menambahkan labels, warna, dan explode
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors, explode=explode)
    ax1.axis('equal')

    # Menampilkan grafik
    st.pyplot(fig1)

with batang:
    fig = px.bar(data, x=f"Category {category}", y=f"Purchase Amount (USD) Size {size}", color=colors)
    st.plotly_chart(fig)

with tabel:
    df = pd.DataFrame(data)
    st.markdown(
        '<div style="margin-top: 20px;"></div>',
        unsafe_allow_html=True
    )
    filtered_df = df[[f"Category {category}", f"Purchase Amount (USD) Size {size}"]]
    st.write(filtered_df)
