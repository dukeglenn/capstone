import streamlit as st

# Set the page layout to wide
st.set_page_config(page_title="Astraea", layout="wide")

# Custom CSS for styling the navbar and adding a 100px buffer at the top
st.markdown("""
    <style>
        /* Ensure body has no margin/padding */
        body {
            margin: 0;
            padding: 0;
        }

        /* Navbar Styling */
        .topnav {
            background-color: #031a2d;
            overflow: hidden;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            padding: 10px 20px;
            width: 100%;
        }

        .topnav a {
            color: white;
            text-decoration: none;
            padding: 14px 16px;
            font-size: 17px;
            font-weight: bold;
            transition: background-color 0.3s, color 0.3s;
        }

        .topnav a:hover {
            background-color: #efcf96;
            color: #031a2d;
        }

        .topnav a.active {
            background-color: #4584a4;
            color: white;
        }

        /* Buffer to push everything down, including navbar */
        .main-container {
            margin-top: 10px; /* 10px buffer applied to navbar & content */
        }

        .left-section {
            background: 
                linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.8)), 
                url('Astraea_Logo.jpg'); 
            background-size: cover;
            background-position: center;
            border-radius: 10px;
            padding: 20px;
            color: white;
        }

        /* Text Overlay */
        .text-box {
            background: rgba(0, 0, 0, 0.6); /* Dark overlay for better readability */
            padding: 15px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Space below navbar to avoid content being hidden
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
    <div class="topnav">
        <a class="active" href="#">Astraea</a>
        <a href="#">Contact</a>
        <a href="#">About</a>
    </div>
""", unsafe_allow_html=True)

# Layout with two columns
col1, col2 = st.columns([1, 1])  # Adjust ratio as needed

# Left section - Welcome message
with col1:
    st.header("Welcome to Astraea")
    st.write("""
        Astraea is committed to enhancing the legal landscape by harnessing the power of 
        machine learning to provide clear, data-driven insights on legal case outcomes 
        and financial information. We empower individuals and families to make informed 
        decisions and connect them to the right legal solutions and professionals, 
        making justice more accessible and transparent for all.
    """)
    st.button("About Us")

# Right section - User input box
with col2:
    problem = st.text_area("Tell us about your issue")

    dropdown1 = st.selectbox("Select an crash type", ['Single Vehicle', 'Two Vehicles', 'Three or More Vehicles'])

    if dropdown1 == 'Two Vehicles':
        dropdown4 = st.selectbox("Select crash type", ['Rear End Collision', 'T-Bone Collision', 'Side to Side', 'Head-On Collision', 'Other'])

    dropdown2 = st.selectbox('Select Number of Passengers in your vehicle', ['1', '2', '3','4+'])
    dropdown3 = st.selectbox('ORIENTATION PLACEHOLDER', ['Driving Straight', 'Stopped', 'Merging', 'Turning Left', 'Turning Right'])
