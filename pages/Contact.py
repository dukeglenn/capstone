import streamlit as st

# Set page config
st.set_page_config(page_title="Contact | Astraea", layout="wide")

# Page title
st.markdown("<h1 style='color: white; text-align: center;'>Contact the Astraea Team</h1>", unsafe_allow_html=True)
st.markdown("##", unsafe_allow_html=True)

# Team data
team = [
    {
        "name": "Killian Daly",
        "email": "kdaly3@tulane.edu",
        "linkedin": "https://www.linkedin.com/in/killian-daly-b6145022a/"
    },
    {
        "name": "Duke Glenn",
        "email": "bglenn@tulane.edu",
        "linkedin": "https://www.linkedin.com/in/dukeglenn/"
    },
    {
        "name": "Henry Miller",
        "email": "hmiller11@tulane.edu",
        "linkedin": "https://www.linkedin.com/in/henry--miller/"
    },
    {
        "name": "Reid Miller",
        "email": "rmiller14@tulane.edu",
        "linkedin": "https://www.linkedin.com/in/reidcmiller/"
    }
]

# Custom CSS
st.markdown("""
    <style>
        .contact-card {
            background-color: #031a2d;
            color: white;
            border-radius: 15px;
            padding: 25px;
            margin: 10px;
            text-align: center;
            box-shadow: 0px 0px 10px #00000055;
        }
        .contact-name {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .contact-email, .linkedin-link {
            font-size: 16px;
            margin-top: 8px;
            display: block;
        }
        .linkedin-icon {
            width: 24px;
            height: 24px;
            margin-top: 5px;
        }
        a {
            color: white;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Layout: 4 team members
cols = st.columns(4)

# Generate contact cards
for i, member in enumerate(team):
    with cols[i]:
        st.markdown(f"""
            <div class="contact-card">
                <div class="contact-name">{member['name']}</div>
                <a class="contact-email" href="mailto:{member['email']}">{member['email']}</a>
                <a class="linkedin-link" href="{member['linkedin']}" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" class="linkedin-icon">
                </a>
            </div>
        """, unsafe_allow_html=True)
