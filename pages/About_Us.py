import streamlit as st

st.set_page_config(page_title="About Us", layout="wide")
st.title("About Us")

team_members = [
    {
        "name": "Killian Daly",
        "hometown": "Irvington, NY",
        "bio": "Killian Daly is a Tulane senior (class of 2025), double majoring in computer science and political science, with a minor in strategic management.  He enjoys analyzing geopolitical shifts and new policy developments, especially at the intersection of  technology and the law. He has worked for the  New York State Supreme Court as a legal researcher, and Northwestern University's Deportation Research Clinic as a project manager and chief data engineer. Killian aims to pursue law school and hopes to contribute to the development of ethical policy solutions in the digital age. In his spare time he enjoys guitar and creative writing.",
        "image": "images/KillianPic.png"
    },
    {
        "name": "Duke Glenn",
        "hometown": "Atlanta, GA",
        "bio": "Duke Glenn is a senior at Tulane majoring in Finance and Computer Science. He plans on attending law school in the near future and working towards a career in intellectual property protection. He enjoys analyzing the intersection between cutting-edge technology and the law, and hopes to further explore this area.",
        "image": "images/DukePic.png"
    },
    {
        "name": "Henry Miller",
        "hometown": "Short Hills, NJ",
        "bio": "Henry is graduating with a triple major in Mathematics, Computer Science, and Economics. He has hands-on experience in data analytics and product operations, having worked with teams across trading, marketing, and finance at Betr. Henry thrives in fast-paced environments, bringing a sharp analytical mindset, strong technical skills, and a collaborative approach to solving complex problems. His recent work includes applying machine learning techniques to build tools that deliver actionable insights",
        "image": "images/HenryPic.png"
    },
    {
        "name": "Reid Miller",
        "hometown": "St Louis, MO",
        "bio": "Reid Miller is a senior at Tulane majoring in Economics, Mathematics, and Computer Science with a minor in Political Science. On campus, he has served as a Vice President of the university’s chapter of Alpha Kappa Psi, a professional business fraternity, and as Director of Training for the Model United Nations team. Upon graduation, he will join RSM’s Chicago headquarters as a consultant in their Enterprise Resource Planning (ERP) practice, with plans to pursue graduate studies in Economics in the future.",
        "image": "images/ReidPic.png"
    }
]

cols = st.columns(4)

for i, member in enumerate(team_members):
    with cols[i]:
        st.image(member["image"], width=400)  # Adjust width as needed
        st.subheader(member["name"])
        st.write(f"**Hometown:** {member['hometown']}")
        st.write(member["bio"])