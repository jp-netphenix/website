import streamlit as st


st.set_page_config(page_title="Projects-NetPhenix",
                   page_icon=":books:", layout="wide")

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
        st.markdown("# Projects")
    with col_2:
        st.image("images/netphenix_logo.png", width=200)
    st.write("---")

# with st.container():
#     col_1, col_2 = st.columns((2, 2))
#     with col_1:
#         st.markdown("## NPTEL")
#     with col_2:
#         text = "Challenges"
#         chn_office = f'<h5> <div>{text}</div></h5>'
#         st.markdown(chn_office, unsafe_allow_html=True)
#         st.write(
#             """
#             - To be done
#             """
#         )

#         text = "Solution"
#         chn_office = f'<h5> <div>{text}</div></h5>'
#         st.markdown(chn_office, unsafe_allow_html=True)
#         st.write(
#             """
#             - To be done
#             """
#         )

#         text = "Value Addition to the customer"
#         chn_office = f'<h5> <div>{text}</div></h5>'
#         st.markdown(chn_office, unsafe_allow_html=True)
#         st.write(
#             """
#             - To be done
#             """
#         )
#     st.write("---")

# with st.container():
#     col_1, col_2 = st.columns((2, 2))
#     with col_1:
#         st.markdown("## Loksabha")
#     with col_2:
#         text = "Challenges"
#         chn_office = f'<h5> <div>{text}</div></h5>'
#         st.markdown(chn_office, unsafe_allow_html=True)
#         st.write(
#             """
#             - To be done
#             """
#         )

#         text = "Solution"
#         chn_office = f'<h5> <div>{text}</div></h5>'
#         st.markdown(chn_office, unsafe_allow_html=True)
#         st.write(
#             """
#             - To be done
#             """
#         )

#         text = "Value Addition to the customer"
#         chn_office = f'<h5> <div>{text}</div></h5>'
#         st.markdown(chn_office, unsafe_allow_html=True)
#         st.write(
#             """
#             - To be done
#             """
#         )
#     st.write("---")

# with st.container():
#     col_1, col_2 = st.columns((2, 2))
#     with col_1:
#         st.markdown("## CMDB")
#     with col_2:
#         text = "Challenges"
#         chn_office = f'<h5> <div>{text}</div></h5>'
#         st.markdown(chn_office, unsafe_allow_html=True)
#         st.write(
#             """
#             - To be done
#             """
#         )

#         text = "Solution"
#         chn_office = f'<h5> <div>{text}</div></h5>'
#         st.markdown(chn_office, unsafe_allow_html=True)
#         st.write(
#             """
#             - To be done
#             """
#         )

#         text = "Value Addition to the customer"
#         chn_office = f'<h5> <div>{text}</div></h5>'
#         st.markdown(chn_office, unsafe_allow_html=True)
#         st.write(
#             """
#             - To be done
#             """
#         )
#     st.write("---")

with st.container():
    col_1, col_2 = st.columns((2, 2))
    with col_1:
        st.markdown("## Digital Media Analytics")
    with col_2:
        text = "Challenges"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Several disparate sources of digital data
            - Data from Google Adwords, Google Analytics, Bing, Facebook, etc.
            - No single source of truth to clients
            """
        )

        text = "Solution"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Leveraged our platform to a dashboard that integrates data from all sources
            - Simple, intuitive dashboard
            - Display various analytics that enables client with spend optimization and sales process
            - Days in market
            - Cost/conversion by media source
            """
        )

        text = "Value Addition to the customer"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Optimize media spend based on cost/conversion opposed to cost/lead
            - Offers to prospects when they are close to purchase
            - Increased close rates and decreased Cost/Conversion
            """
        )

    st.write("---")

with st.container():
    col_1, col_2 = st.columns((2, 2))
    with col_1:
        st.markdown("## Lead Management Analytics")
    with col_2:
        text = "Challenges"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Several disparate sources for leads
            - Sales in CRM, separate from leads
            """
        )

        text = "Solution"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Develop a dashboard that pulls data from all sources containing leads data
            - Pull sales data from CRM
            - Tie leads to sales
            - Display various analytics that enables client with spend optimization and sales process
            - Days in market
            - Cost/conversion by media source
            """
        )

        text = "Value Addition to the customer"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Optimize media spend based on cost/conversion opposed to cost/lead
            - Offers to prospects when they are close to purchase
            - Increased close rates and decreased Cost/Conversion
            """
        )
    st.write("---")

with st.container():
    col_1, col_2 = st.columns((2, 2))
    with col_1:
        st.markdown("## F-F Battery Monitoring")
    with col_2:
        text = "Challenges"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - To maintain the complete lifecycle of a battery from Formation to Finishing
            - Tracing the battery
            """
        )

        text = "Solution"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Tracking the battery status from formation to finishing
            - Integration with Multimeter and mobile for reading data and store the data into cloud
            - Logging the each battery voltage in various stages
            - QR code scanning 
            - Traceability report 
            - Rack management
            """
        )

        text = "Value Addition to the customer"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Get rid of taking manual reading of batteries 
            - Battery traceability from formation to finishing in seconds
            - Identifying the batteries/Tag in a Rack
            """
        )
    st.write("---")

with st.container():
    col_1, col_2 = st.columns((2, 2))
    with col_1:
        st.markdown("## Warehouse Battery Tracking")
    with col_2:
        text = "Challenges"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Automate the voltage measurement and recording
            - Single portal for across India
            - Battery tracing after customer delivery
            """
        )

        text = "Solution"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Battery identification through barcode/QR code scanner
            - Monitoring the battery data
            - Storing the measurement data in a single place
            - Security is through login credentials to access data
            - Mobile app for measurements 
            - Web portal for view & report
            """
        )

        text = "Value Addition to the customer"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Get rid of taking manual reading of batteries 
            - Battery traceability in seconds
            - Warehouse wise report
            """
        )
    st.write("---")

with st.container():
    col_1, col_2 = st.columns((2, 2))
    with col_1:
        st.markdown("## Connected Vehicle")
    with col_2:
        text = "Challenges"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Electric assist drive
            - Cardio sense system
            - Vehicle telematics
            """
        )

        text = "Solution"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Live data tracking
            - Vehicle telematics
            - Raider telematics
            - Cardio sense system integration
            - Manual, Auto and Hill mode
            - Content emergency SOS
            - Service notification
            - Anti theft alarm & User security
            """
        )

        text = "Value Addition to the customer"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Monitor end-to-end (From manufacturing to customer usage)
            - Connected intelligence 
            - Reports
            """
        )
    st.write("---")

with st.container():
    col_1, col_2 = st.columns((2, 2))
    with col_1:
        st.markdown("## Corrosion Control System")
    with col_2:
        text = "Challenges"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Controlling corrosion in a ship is a manual process
            """
        )

        text = "Solution"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - We Build a hardware agent, which via IoT enables communication with ANodes
            - Data gets collected from agents into the IoT platform
            - Auto control of Current and Voltage
            """
        )

        text = "Value Addition to the customer"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Inference on cumulative damage sustained (retrospective) and the prevailing corrosion rate (real time and continuous)
            - Current status of the ANode
            - Alarm notification on threshold limits
            """
        )
    st.write("---")

with st.container():
    col_1, col_2 = st.columns((2, 2))
    with col_1:
        st.markdown("## Robots In Special Education")
    with col_2:
        text = "Challenges"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Training children with Autism
            - Monitoring children's activity for further improvements
            """
        )

        text = "Solution"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Control/managing the robots
            - Measuring the performance of child for all activities 
            - Feedback mechanism
            """
        )

        text = "Value Addition to the customer"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Easy training
            - Automatic measuring of skills  
            - Increase the training efficiency
            """
        )
    st.write("---")

with st.container():
    col_1, col_2 = st.columns((2, 2))
    with col_1:
        st.markdown("## Network Trouble Ticketing")
    with col_2:
        text = "Challenges"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Ticket assignment to user
            - SLA violation
            - Unable to collaborate with teams
            - No knowledge base 
            """
        )

        text = "Solution"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Streamline all customer conversations in one place
            - Automate repetitive work and save time
            - Collaborate with other teams to resolve issues faster
            - Parent-Child ticketing
            - Centralised knowledge base
            - Reports and Dashboards
            """
        )

        text = "Value Addition to the customer"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Intelligent ticket assignment
            - Shared ownership of tickets
            - Automatically suggest solutions
            - Auto email notification
            """
        )
    st.write("---")

with st.container():
    col_1, col_2 = st.columns((2, 2))
    with col_1:
        st.markdown("## Capturing Remote Desktop")
    with col_2:
        text = "Challenges"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Screen Capture all user activities performed in remote session
            - Provide visibility for user activities
            """
        )

        text = "Solution"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Capturing the remote desktop sessions
            - Log the screen capture 
            - Send captured images as live video to the server as MP4
            - Playback the captured sessions
            """
        )

        text = "Value Addition to the customer"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Send login and logout notification to server using REST api calls
            - Integration with existing system
            """
        )
    st.write("---")

with st.container():
    col_1, col_2 = st.columns((2, 2))
    with col_1:
        st.markdown("## Text Mining - Pharma")
    with col_2:
        text = "Challenges"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - Want to know the trend of Zika virus
            - Data is available in PDF, DOC, Web, FB, Twitter, Google etc
            - No single source of truth for client
            """
        )

        text = "Solution"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            Developed a dashboard that provides the analysis below
            - Word Cloud
            - Co-occurrence Graph
            - Bi-grams & Tri-grams
            - Text Tree
            - Top performing associate keywords
            - Sentiment Analysis
            """
        )

        text = "Value Addition to the customer"
        chn_office = f'<h5> <div>{text}</div></h5>'
        st.markdown(chn_office, unsafe_allow_html=True)
        st.write(
            """
            - To be added
            """
        )
    st.write("---")
