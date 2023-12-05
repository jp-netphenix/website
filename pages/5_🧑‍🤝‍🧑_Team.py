import streamlit as st

st.set_page_config(page_title="Team-NetPhenix",
                   page_icon=":people_holding_hands:", layout="wide")

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
        st.markdown("# Our Team")
    with col_2:
        st.image("images/netphenix_logo.png", width=200)
    st.write("---")


with st.container():
    col_1, col_2, col_3, col_4, col_5 = st.columns((1, 1, 1, 1, 1))
    with col_2:
        st.image("images/staff/tag.jpeg")
        text = "Our Mentor"
        title = f"<h5><div style='text-align: center;'>{text}</div></h5>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Dr. Timothy A. Gonsalves"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Former Director IIT Mandi"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_3:
        st.image("images/staff/jp.jpeg")
        text = "Jayaprakash"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "CEO"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_4:
        st.image("images/staff/sam.jpeg")
        text = "Varghees"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "CTO"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    st.write("---")

with st.container():
    col_1, col_2, col_3, col_4, col_5 = st.columns((1, 1, 1, 1, 1))
    with col_1:
        st.image("images/staff/Abhi.jpg")
        text = "Arul"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Sr. Software Engineer"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_2:
        st.image("images/staff/santhosh.jpg")
        text = "Shanthosh"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Sr. System Admin"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_3:
        st.image("images/staff/Shanker.png")
        text = "Shanker"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Project Manager"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_4:
        st.image("images/staff/Ashick.jpg")
        text = "Ashick"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Sr. Software Engineer"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_5:
        st.image("images/staff/Jerone.jpg")
        text = "Jerone"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Sr. Software Engineer"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    st.write("#")


with st.container():
    col_1, col_2, col_3, col_4, col_5 = st.columns((1, 1, 1, 1, 1))
    with col_1:
        st.image("images/staff/Abhi.jpg")
        text = "Sandheep"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Software Engineer"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_2:
        st.image("images/staff/Abhi.jpg")
        text = "Abhi"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Software Engineer"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_3:
        st.image("images/staff/Mukesh.jpg")
        text = "Mukesh"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Software Engineer"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_4:
        st.image("images/staff/Aravind.jpg")
        text = "Aravind"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Software Engineer"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_5:
        st.image("images/staff/Cilin-new.png")
        text = "Cilin"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Software Engineer"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    st.write("#")

with st.container():
    col_1, col_2, col_3, col_4, col_5 = st.columns((1, 1, 1, 1, 1))

    with col_1:
        st.image("images/staff/Bibino.jpg")
        text = "Bibino"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "Software Engineer"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_2:
        st.image("images/staff/Abish.jpg")
        text = "Abish"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "QA Engineer"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
    with col_3:
        st.image("images/staff/SaiKrishna.jpg")
        text = "Saikrishna"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
        text = "QA Engineer"
        title = f"<h6><div style='text-align: center;'>{text}</div></h6>"
        st.markdown(title, unsafe_allow_html=True)
