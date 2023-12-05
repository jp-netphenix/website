import streamlit as st

st.set_page_config(page_title="Contact-NetPhenix",
                   page_icon=":handshake:", layout="wide")

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


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ---- CONTACT ----
with st.container():
    col_1, col_2 = st.columns((4, 1))
    with col_1:
        st.markdown("# Get In Touch With Us! ")
    with col_2:
        st.image("images/netphenix_logo.png", width=200)
    st.write("---")

with st.container():
    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
        <form action="https://formsubmit.co/info@netphenix.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        text = "Kanyakumari Office: "
        kk_office = f'<h5> <div style="text-align: center;">{text}</div></h5>'
        st.markdown(kk_office, unsafe_allow_html=True)
        address = """
            <div style="text-align: center;">
            Koyickal Thoppu, Near RC Church
            <p>Kanjampuram Post Kanyakumari District, 
            India. Pin: 629 154
            </div>
            """
        st.markdown(address, unsafe_allow_html=True)

        text = "Chennai Office: "
        chn_office = f'<h5> <div style="text-align: center;">{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        address = """
            <div style="text-align: center;">
            CASAGRANDE,
            C5 First floor, 49 Ellaiammankoil Street,
            <p>Adyar, Chennai, India, Pin: 600 020.
            </div>
            """
        st.markdown(address, unsafe_allow_html=True)
        st.write('##')

        text = "info@netphenix.com +91 99404 47420"
        mail = f'<h6> <div style="text-align: center;">{text}</div></h6>'
        st.markdown(mail, unsafe_allow_html=True)
