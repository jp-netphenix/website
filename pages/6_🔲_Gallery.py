import streamlit as st

st.set_page_config(page_title="Gallery-NetPhenix",
                   page_icon=":black_square_button:", layout="wide")

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
            
        <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)


with st.container():
    col_1, col_2 = st.columns((4, 1))
    with col_1:
        st.markdown("# Gallery")
    with col_2:
        st.image("images/netphenix_logo.png", width=200)
    st.write("---")

with st.container():
    col_1, col_2 = st.columns((5, 1))
    with col_1:
        st.image("images/gallery/shanker_wedding.JPG")
    with col_2:
        text = "Shanker Wedding at Nithravalai"
        st.write(text)
        st.write("14 May, 2023")
    st.write("---")

with st.container():
    col_1, col_2 = st.columns((5, 1))
    with col_1:
        st.image("images/gallery/santhosh_wedding.png")
    with col_2:
        text = "Santhosh Wedding at Nithravalai"
        st.write(text)
        st.write("29 Aug, 2022")
    st.write("---")


with st.container():
    col_1, col_2 = st.columns((5, 1))
    with col_1:
        st.image("images/gallery/outing_1.jpg")
    with col_2:
        text = "Outing"
        st.write(text)
        st.write("28 Jan, 2023")
    st.write("---")
