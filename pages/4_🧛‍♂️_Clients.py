import streamlit as st

st.set_page_config(page_title="Clients-NetPhenix",
                   page_icon=":vampire:", layout="wide")

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
        st.markdown("# Our Clients")
    with col_2:
        st.image("images/netphenix_logo.png", width=200)
    st.write("---")

with st.container():
    col_1, col_2 = st.columns((1, 2))
    with col_1:
        st.image("images/iit_logo.png", width=100)
    with col_2:
        st.write("The Indian Institute of Technology Madras (IIT Madras) is one of the premier engineering institutes in India. It is located in Chennai, Tamil Nadu, and was established in 1959. IIT Madras is known for its academic excellence, cutting-edge research, and contributions to the fields of science, engineering, and technology.")
    st.write("#")

with st.container():
    col_1, col_2 = st.columns((1, 2))
    with col_1:
        st.image("images/nptel.jpeg", width=170)
    with col_2:
        st.write("NPTEL is an acronym for National Programme on Technology Enhanced Learning which is an initiative by seven Indian Institutes of Technology (IIT Bombay, Delhi, Guwahati, Kanpur, Kharagpur, Madras and Roorkee) and Indian Institute of Science (IISc) for creating course contents in engineering and science.")
        st.write("#")

with st.container():
    col_1, col_2 = st.columns((1, 2))
    with col_1:
        st.image("images/nms_logo.png", width=150)
    with col_2:
        st.write("NMSWorks Software delivers OSS and BSS solutions to some of the largest and most demanding telecom service providers, network equipment vendors and enterprises.")
    st.write("#")

with st.container():
    col_1, col_2 = st.columns((1, 2))
    with col_1:
        st.image("images/dealsplus.png", width=150)
    with col_2:
        st.write(
            "DealsPlus helps private equity, real estate and infrastructure fund managers be transaction ready. Provider of investment deal execution services intended to significantly reduce the time and cost of preparing for transactions. The company helps to standardize and automate the deliverables required at closing, full visibility, and control over both ongoing and event-based compliance obligations, tracks investment structures, compliance obligations, cap tables, and portfolio documents, enabling private equity, real estate, and infrastructure fund managers to strengthen their M&A processes and create a single source of truth across their investment structures.")
        st.write("#")

with st.container():
    col_1, col_2 = st.columns((1, 2))
    with col_1:
        st.image("images/amararaja_logo.png", width=140)
    with col_2:
        st.write("Amara Raja is well-known for manufacturing lead-acid batteries, which find applications in automotive, industrial, and other sectors. They produce batteries for various vehicles, including cars, motorcycles, commercial vehicles, and inverters.")
    st.write("#")

with st.container():
    col_1, col_2 = st.columns((1, 2))
    with col_1:
        st.image("images/pedaleze_logo.png", width=150)
    with col_2:
        st.write("A technology company that focuses on revolutionizing the concept of 'Make in India',  in the mobility and wellness segment.")
    st.write("#")

with st.container():
    col_1, col_2 = st.columns((1, 2))
    with col_1:
        st.image("images/precision_logo.png", width=200)
    with col_2:
        st.write("Established in 1996, Precision provides Biometric, IoT, Cloud & Systems Integration solutions and IT Infrastructure Management Services. Precision adopts a consulting approach to address the needs of clients and has a very strong R&D and IP creation focus. With a PAN India")
    st.write("#")

with st.container():
    col_1, col_2 = st.columns((1, 2))
    with col_1:
        st.image("images/deeta_logo.webp", width=150)
    with col_2:
        st.write("Deeta Analytics is a leading analytics and business intelligence company that helps clients incorporate the use of data analysis in their businesses.")
    st.write("#")

with st.container():
    col_1, col_2 = st.columns((1, 2))
    with col_1:
        st.image("images/myrmc_logo.webp", width=150)
    with col_2:
        st.write("MyRMC is a one stop solution for booking and hiring Transit mixer, Pump and Gang and Boom Plazer in one touch.")

    st.write("---")

# st.balloons()
