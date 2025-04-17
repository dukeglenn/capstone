import streamlit as st

st.set_page_config(page_title="Contact Representation", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .title {
            font-size: 48px;
            font-weight: bold;
            color: #2b576d;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 24px;
            color: #4584a4;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .body-text {
            font-size: 16px;
            color: #333333;
            line-height: 1.6;
        }
        .lawyer-card {
            background-color: #f2f7fa;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            border-left: 4px solid #2b576d;
        }
        .lawyer-name {
            font-size: 20px;
            font-weight: bold;
            color: #2b576d;
        }
        .lawyer-link {
            font-size: 16px;
            color: #4584a4;
            text-decoration: none;
        }
        .lawyer-link:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Page content
st.markdown('<div class="title">Contact Representation</div>', unsafe_allow_html=True)

st.markdown("""
<div class="body-text">
If you've recently experienced an accident and believe you may need legal support, here are some trusted firms you can contact for a consultation. These are not endorsements, but helpful starting points for exploring your options.
</div>
""", unsafe_allow_html=True)

# Lawyer listings
lawyers = [
    {
        "name": "Car Injury Justice – Free Consultation",
        "link": "https://carinjuryjustice.com/free-consultation/v2/location/new-york-car-accident-lawyer?ts=sg4&c=l5&m=p&g=new-york&k=new%20york%20injury%20lawyer&d=c&gad_source=1&gbraid=0AAAAApPU6eoMEnAHa6miap1eE3Lj2B4oD&gclid=Cj0KCQjwqv2_BhC0ARIsAFb5Ac9ExotLtfTWDKqtRuBbXAM9mYuTkK2NjwhMYD74FJfV8XqwYjcNHzoaAnj6EALw_wcB#step-1"
    },
    {
        "name": "Rosenbaum & Rosenbaum, P.C.",
        "link": "https://www.rosenbaumnylaw.com/"
    },
    {
        "name": "Block O’Toole & Murphy, LLP",
        "link": "https://www.blockotoole.com/"
    },
    {
        "name": "Wingate, Russotti, Shapiro & Halperin, LLP",
        "link": "https://www.wrshlaw.com/"
    }
]

for lawyer in lawyers:
    st.markdown(f"""
        <div class="lawyer-card">
            <div class="lawyer-name">{lawyer['name']}</div>
            <a class="lawyer-link" href="{lawyer['link']}" target="_blank">Visit Website</a>
        </div>
    """, unsafe_allow_html=True)
