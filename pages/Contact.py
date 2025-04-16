import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

st.markdown("""
    <style>
        .lawyer-card {
            background: linear-gradient(135deg, #031a2d, #1f2a36);
            border: 1px solid #4a90e2;
            border-radius: 10px;
            padding: 20px;
            color: white;
            text-align: center;
            margin: 10px;
            height: 150px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .lawyer-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(74, 144, 226, 0.6);
        }

        .lawyer-link {
            color: #4a90e2;
            font-weight: bold;
            text-decoration: none;
            font-size: 14px;
            padding: 8px 16px;
            border: 2px solid #4a90e2;
            border-radius: 20px;
            transition: background-color 0.3s ease;
        }

        .lawyer-link:hover {
            background-color: #4a90e2;
            color: white;
        }

        h2 {
            color: white;
            font-size: 18px;
            margin-bottom: 10px;
        }

        .header {
            font-size: 36px;
            font-weight: 700;
            color: white;
            text-align: center;
            margin-bottom: 30px;
        }

        .desc {
            color: #ddd;
            text-align: center;
            margin-bottom: 40px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <h2 style="text-align: center; color: black; font-weight: bold; margin-bottom: 30px;">
        Connect with a Lawyer
    </h2>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="desc">Need legal help after an accident? Use one of the trusted firms below to get started.</div>', unsafe_allow_html=True)

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

cols = st.columns(2)

for idx, lawyer in enumerate(lawyers):
    with cols[idx % 2]:
        st.markdown(f"""
            <div class="lawyer-card">
                <h2>{lawyer['name']}</h2>
                <a class="lawyer-link" href="{lawyer['link']}" target="_blank">Visit Website</a>
            </div>
        """, unsafe_allow_html=True)
