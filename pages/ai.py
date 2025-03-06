import streamlit as st

st.title('NSK Bearing AI')
st.write('NSK-AI will estimate the remaining life of the bearing.')

st.video("images/Demo1.mp4")

st.write('Need more information?')

col1, col2 = st.columns(2)

with col1:
    if st.button('Contact Us'):
        st.write(
            'Please contact us at:[NSK-Corp.](https://www.nsk.com/)')

with col2:
    if st.button('Back to Home'):
        st.switch_page('home.py')
