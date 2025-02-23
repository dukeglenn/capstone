import streamlit as st

# Custom CSS for styling
def custom_css():
    st.markdown(
        """
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                background-color: #03233d;
                color: #f2f2f2;
            }
            .topnav {
                background-color: #031a2d;
                overflow: hidden;
                display: flex;
                justify-content: flex-start;
                padding: 10px;
            }
            .topnav a {
                color: #f2f2f2;
                text-decoration: none;
                padding: 14px 16px;
                font-size: 17px;
            }
            .topnav a:hover {
                background-color: #ddd;
                color: #031a2d;
            }
            .topnav a.active {
                background-color: black;
                color: white;
            }
            .container {
                display: flex;
                justify-content: space-between;
                align-items: stretch;
                padding: 20px;
                height: 80vh;
                gap: 20px;
            }
            .left-section, .right-section {
                flex: 1;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
            }
            .left-section {
                background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.8));
                color: #f2f2f2;
            }
            .about-btn {
                margin: 20px auto;
                padding: 10px 20px;
                font-size: 16px;
                background-color: #04aa6d;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .about-btn:hover {
                background-color: #037d52;
            }
            textarea {
                width: 100%;
                height: 300px;
                padding: 15px;
                font-size: 16px;
                background-color: #031a2d;
                color: #f2f2f2;
                border-radius: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply custom CSS
custom_css()

# Navigation bar
st.markdown(
    """
    <div class="topnav">
        <a class="active" href="#home">Astraea</a>
        <a href="#contact">Contact</a>
        <a href="#about">About</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("## Welcome to Astraea")
    st.write(
        "Committed to enhancing the legal landscape by harnessing the power of machine learning to provide clear, data-driven insights on legal case outcomes and financial information."
    )
    st.button("About Us")

with col2:
    user_input = st.text_area("Tell us about your issue", "")

    if st.button("Submit"):
        st.success("Your issue has been recorded. A legal expert will review it soon.")
