import streamlit as st

st.set_page_config(page_title="About Us", layout="wide")

st.title("Meet the Team")

team_members = [
    {
        "name": "Killian Daly",
        "hometown": "Hometown 1",
        "bio": "This is a short biography of team member 1.",
        "image": "path_to_image_1.jpg"
    },
    {
        "name": "Duke Glenn",
        "hometown": "Hometown 2",
        "bio": "This is a short biography of team member 2.",
        "image": "path_to_image_2.jpg"
    },
    {
        "name": "Henry Miller",
        "hometown": "Hometown 3",
        "bio": "This is a short biography of team member 3.",
        "image": "path_to_image_3.jpg"
    },
    {
        "name": "Reid Miller",
        "hometown": "Hometown 4",
        "bio": "This is a short biography of team member 4.",
        "image": "path_to_image_4.jpg"
    }
]

cols = st.columns(4)

for col, member in zip(cols, team_members):
    with col:
        st.image(member["image"], caption=member["name"], use_column_width=True)
        st.subheader(member["name"])
        st.write(f"**Hometown:** {member['hometown']}")
        st.write(member["bio"])
