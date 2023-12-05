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
