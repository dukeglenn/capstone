import streamlit as st

# Set the page layout to wide
st.set_page_config(page_title="Astraea", layout="wide")

st.markdown("""
    <style>
        body {
            background-color: #2b576d !important;
        }
    </style>
""", unsafe_allow_html=True)

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
# Left Section - Background Image with Overlay Text
with col1:
    # Load an image (Replace with your actual image path)
    image_url = "Astraea_Logo.png"  # Example image
    st.image(image_url, use_container_width=True)

    # Overlay Text (Placed in a markdown box)
    st.markdown("""
        <div style="
            position: relative; 
            top: -250px; 
            background: rgba(0, 0, 0, 0.6); 
            padding: 20px; 
            border-radius: 10px;
            color: white;
            text-align: center;">
            <h1>Welcome to Astraea</h1>
            <p>
                Astraea is committed to enhancing the legal landscape by harnessing the power of 
                machine learning to provide clear, data-driven insights on legal case outcomes 
                and financial information. We empower individuals and families to make informed 
                decisions and connect them to the right legal solutions and professionals, 
                making justice more accessible and transparent for all.
            </p>
        </div>
    """, unsafe_allow_html=True)
# Right section - User input box
with col2:
    problem = st.text_area("Tell us about your issue")

    dropdown1 = st.selectbox("Select an crash type", ['Single Vehicle', 'Two Vehicles', 'Three or More Vehicles'])

    if dropdown1 == 'Two Vehicles':
        dropdown4 = st.selectbox("Select crash type", ['Rear End Collision', 'T-Bone Collision', 'Side to Side', 'Head-On Collision', 'Other'])

    dropdown2 = st.selectbox('Select Number of Passengers in your vehicle', ['1', '2', '3','4+'])
    dropdown3 = st.selectbox('ORIENTATION PLACEHOLDER', ['Driving Straight', 'Stopped', 'Merging', 'Turning Left', 'Turning Right'])
    if st.button("Submit"):
        st.success("Your issue has been recorded. A legal expert will review it soon.")