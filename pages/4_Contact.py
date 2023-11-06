import streamlit as st

# Menambahkan title dan icon pada page
st.set_page_config(
    page_title="Contact",
    page_icon="🐼"
)
# Menambahkan gambar di sidebar
st.sidebar.markdown(
    '<div style="display: flex; justify-content: center; position: fixed; top: 0; width: 23%; height: 12%; margin-top: 1%;">'
    '<img src="https://i.pinimg.com/564x/31/56/7a/31567a2aea11c60f3792b2f9d09d1dde.jpg" style="object-fit: cover; width: 75px; height: 75px; border-radius: 50%; overflow: hidden;">'
    '</div>',
    unsafe_allow_html=True
)
# Menambahkan gambar di samping Address
st.markdown(
        '<div style="display: flex; justify-content: left; position: absolute; top: 0; width: 7%; height: 10%; margin-top: 42%;">'
        '<img src="https://i.pinimg.com/564x/2b/3f/59/2b3f5903e6ef99075ab2f2fee8c11763.jpg" style="object-fit: cover; width: 40px; height: 40px; border-radius: 50%; overflow: hidden;">'
        '</div>',
        unsafe_allow_html=True
    )
# Menambahkan gambar di samping Phone
st.markdown(
        '<div style="display: flex; justify-content: left; position: absolute; top: 0; width: 7%; height: 10%; margin-top: 55%;">'
        '<img src="https://i.pinimg.com/564x/8d/e5/50/8de5507d6f51f9c8b64d90c175c0b1e5.jpg" style="object-fit: cover; width: 40px; height: 40px; border-radius: 50%; overflow: hidden;">'
        '</div>',
        unsafe_allow_html=True
    )
# Menambahkan gambar di samping Email
st.markdown(
        '<div style="display: flex; justify-content: left; position: absolute; top: 0; width: 7%; height: 10%; margin-top: 64%;">'
        '<img src="https://i.pinimg.com/564x/45/af/cb/45afcb072e032c54b0dfc739e67d25ab.jpg" style="object-fit: cover; width: 40px; height: 40px; border-radius: 50%; overflow: hidden;">'
        '</div>',
        unsafe_allow_html=True
    )

def main():
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
    # Mengatur font-size, font-family, dan text berada di tengah
    st.markdown(
        '<div style="text-align: center; font-size: 60px; font-family: timesnewroman;">Contact Us</div>'
        '<div style="text-align: center; font-size: 19px; font-family: timesnewroman;">Silahkan hubungi kami jika anda mengalami kendala atau masalahan terkait informasi atau hal lainnya saat mengunjungi dashboard kami</div>',
        unsafe_allow_html=True
    )
    # Membuat 2 column
    col1, col2 = st.columns(2)

    # Menambahkan konten ke setiap kolom
    with col1: # Column 1 berisi data tentang alamat, phone, dan email
        st.markdown(
            '<div style="font-size: 20px; font-family: timesnewroman; color: cyan; margin-top: 70px; margin-left: 50px;">Address</div>'
            '<div style="font-size: 15px; font-family: timesnewroman; margin-left: 50px;">4671 Sugar Camp Road,<br>Owatonna, Minnesota</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 20px; font-family: timesnewroman; color: cyan; margin-top: 25px; margin-left: 50px;">Phone</div>'
            '<div style="font-size: 15px; font-family: timesnewroman; margin-left: 50px;">(+62) 89-668-276-136</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size: 20px; font-family: timesnewroman; color: cyan; margin-top: 25px; margin-left: 50px;">Email</div>'
            '<div style="font-size: 15px; font-family: timesnewroman; margin-left: 50px;">pengangguran_163@gmail.com</div>',
            unsafe_allow_html=True
        )

    with col2: # Column 2 untuk mengirimkan pesan jika mengalami kendala
        st.markdown(
            '<div style="font-size: 20px; font-family: timesnewroman; margin-top: 70px; color: plum;">Send Message</div>',
            unsafe_allow_html=True
        )
        name = st.text_input("Name")
        email = st.text_input("Email")
        description = st.text_area("Description")

        if st.button("Send"):
            if name and email and description:  # Memastikan semua input terisi
                st.success("Your message has been sent!")
                st.write("Name:", name)
                st.write("Email:", email)
                st.write("Description:", description)
            else:
                st.warning("Please fill in all fields.")

if __name__ == '__main__':

    main()