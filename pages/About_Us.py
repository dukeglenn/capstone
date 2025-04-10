import streamlit as st

st.set_page_config(page_title="Legal Info", layout="wide")

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
    </style>
""", unsafe_allow_html=True)

# Content
st.markdown('<div class="title">Legal Information</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">Disclaimer</div>', unsafe_allow_html=True)
st.markdown("""
<div class="body-text">
The information provided by Astraea is for general informational purposes only and should not be construed as legal advice. 
While our predictions are based on data-driven models and historical cases, they do not account for the full complexity of any specific legal situation.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="subtitle">No Attorney-Client Relationship</div>', unsafe_allow_html=True)
st.markdown("""
<div class="body-text">
Use of this platform does not create an attorney-client relationship. If you require legal assistance, we recommend contacting a licensed attorney in your jurisdiction.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="subtitle">Data Sources</div>', unsafe_allow_html=True)
st.markdown("""
<div class="body-text">
Our predictions are generated using publicly available legal datasets and machine learning algorithms. All efforts are made to ensure the accuracy of the data, but results are not guaranteed.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="subtitle">Privacy Policy</div>', unsafe_allow_html=True)
st.markdown("""
<div class="body-text">
We value your privacy. No personal or case-specific information is stored or shared through the Astraea platform unless explicitly authorized by the user.
</div>
""", unsafe_allow_html=True)