import streamlit as st

st.set_page_config(page_title="About Us", layout="wide")

st.markdown("""
    <style>
        .profile-card {
            text-align: center;
            padding: 10px;
        }
        .name {
            font-size: 20px;
            font-weight: bold;
            margin-top: 10px;
        }
        .hometown {
            font-size: 16px;
            color: #ccc;
        }
        .bio {
            font-size: 15px;
            margin: 10px 0;
        }
        .contact-icons a {
            margin: 0 8px;
            text-decoration: none;
        }
        .icon {
            height: 24px;
            vertical-align: middle;
        }
    </style>
""", unsafe_allow_html=True)

st.title("About Us")

team = [    
    {
        "name": "Killian Daly",
        "hometown": "Irvington, NY",
        "bio": "Killian Daly is a Tulane senior (class of 2025), double majoring in computer science and political science, with a minor in strategic management.  He enjoys analyzing geopolitical shifts and new policy developments, especially at the intersection of  technology and the law. He has worked for the  New York State Supreme Court as a legal researcher, and Northwestern University's Deportation Research Clinic as a project manager and chief data engineer. Killian aims to pursue law school and hopes to contribute to the development of ethical policy solutions in the digital age. In his spare time he enjoys guitar and creative writing.",
        "image": "images/KillianPic.png",
        "email": "kdaly3@tulane.edu",
        "linkedin": "https://www.linkedin.com/in/killian-daly-b6145022a/"
    },
    {
        "name": "Duke Glenn",
        "hometown": "Atlanta, GA",
        "bio": "Duke Glenn is a senior at Tulane majoring in Finance and Computer Science. He plans on attending law school in the near future and working towards a career in intellectual property protection. He enjoys analyzing the intersection between cutting-edge technology and the law, and hopes to further explore this area.",
        "image": "images/DukePic.png",
        "email": "bglenn@tulane.edu",
        "linkedin": "https://www.linkedin.com/in/dukeglenn/"
    },
    {
        "name": "Henry Miller",
        "hometown": "Short Hills, NJ",
        "bio": "Henry is graduating with a triple major in Mathematics, Computer Science, and Economics. He has hands-on experience in data analytics and product operations, having worked with teams across trading, marketing, and finance at Betr. Henry thrives in fast-paced environments, bringing a sharp analytical mindset, strong technical skills, and a collaborative approach to solving complex problems. His recent work includes applying machine learning techniques to build tools that deliver actionable insights",
        "image": "images/HenryPic.png",
        "email": "hmiller11@tulane.edu",
        "linkedin": "https://www.linkedin.com/in/henry--miller/"
    },
    {
        "name": "Reid Miller",
        "hometown": "St Louis, MO",
        "bio": "Reid Miller is a senior at Tulane majoring in Economics, Mathematics, and Computer Science with a minor in Political Science. On campus, he has served as a Vice President of the university’s chapter of Alpha Kappa Psi, a professional business fraternity, and as Director of Training for the Model United Nations team. Upon graduation, he will join RSM’s Chicago headquarters as a consultant in their Enterprise Resource Planning (ERP) practice, with plans to pursue graduate studies in Economics in the future.",
        "image": "images/ReidPic.png",
        "email": "rmiller14@tulane.edu",
        "linkedin": "https://www.linkedin.com/in/reidcmiller/"
    }
]

cols = st.columns(4)

for i, member in enumerate(team):
    with cols[i]:
        st.markdown(f"<div class='profile-card'>", unsafe_allow_html=True)
        st.image(member["image"], width=200)
        st.markdown(f"<div class='name'>{member['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='hometown'>{member['hometown']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='bio'>{member['bio']}</div>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class='contact-icons'>
                <a href='mailto:{member['email']}' target='_blank'>
                    <img src='https://img.icons8.com/material-outlined/24/email--v1.png' class='icon'/>
                </a>
                <a href='{member['linkedin']}' target='_blank'>
                    <img src='https://img.icons8.com/ios-filled/24/linkedin.png' class='icon'/>
                </a>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)