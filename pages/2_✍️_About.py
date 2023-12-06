import streamlit as st

st.set_page_config(page_title="About-NetPhenix",
                   page_icon=":writing_hand:",
                   layout="wide")

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
        st.markdown("# About")
    with col_2:
        st.image("images/netphenix_logo.png", width=200)
    st.write("---")

with st.container():
    text = "Customized Software Development Solutions in India"
    title = f"<h5> <div style='text-align: center;'>{text}</div></h5>"
    st.markdown(title, unsafe_allow_html=True)
    st.write("Experience tailored software development designed to meet the unique requirements of your business. Unlike off-the-shelf solutions that force you to adjust your processes, our custom applications are meticulously crafted to seamlessly integrate with your business environment.")
    st.write("#")

with st.container():
    text = "Why Choose Us?"
    title = f"<h5> <div>{text}</div></h5>"
    st.markdown(title, unsafe_allow_html=True)
    st.write("At NetPhenix, we prioritize client satisfaction by working in your time zone. Operating from a tier two city in India, we offer cost-effective solutions. Our comprehensive range of services includes major development, design, and SEO services, all conveniently available under one roof. Benefit from a dedicated team of highly skilled and experienced professionals.")
    st.write("#")

with st.container():
    text = "Our Services"
    title = f"<h5> <div>{text}</div></h5>"
    st.markdown(title, unsafe_allow_html=True)
    st.write("Our operational foundation is built on three core principles:")
    st.write("- Timely Delivery")
    st.write("- Client Satisfaction")
    st.write("- Affordable Rates")
    st.write("#")

with st.container():
    text = "Vision and Mission"
    title = f"<h5> <div>{text}</div></h5>"
    st.markdown(title, unsafe_allow_html=True)
    st.write("Vision:")
    st.write("To emerge as a leader in the SME segment, delivering cost-effective coding solutions and serving as a one-stop solution provider for a diverse range of products. We strive to provide high-quality Website Development in India with quick turnaround times and competitive pricing for onshore and offshore customers.")
    st.write("Mission:")
    st.write('Our mission is to be a technological translator in the market, ensuring satisfaction and service excellence. We aim to plan, build, and establish ourselves as a premier IT service provider. Our belief is encapsulated in the mantra, "Hold your customer today, and they will hold you tomorrow till you exist." Building strong relationships with our customers is our commitment, always delivering the best.')
    st.write("#")
