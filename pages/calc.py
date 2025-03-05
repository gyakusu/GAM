import streamlit as st

st.title('NSK Bearing Calculator')
st.write('Please input the dimensions of the bearing you want to calculate.')

st.image('images/Calc0.png', use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    if st.button('Calculate With AI'):
        st.switch_page('ai.py')

with col2:
    if st.button('Back to Home'):
        st.switch_page('home.py')
