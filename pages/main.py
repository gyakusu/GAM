import streamlit as st

st.markdown(
    """
    <style>
    .fixed-button {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 1000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="fixed-button">
        <button onclick="document.getElementById('cart_button').click()">Add to cart</button>
    </div>
    """,
    unsafe_allow_html=True
)

cart_button = st.button("Add to cart", key="cart_button",
                        icon=":material/shopping_cart:")

if cart_button:
    st.write("Added to cart!")

home = st.Page("home.py", title="Home", icon=":material/home:")

calc = st.Page("calc.py", title="Calculate-Operation",
               icon=":material/calculate:")

ai = st.Page("ai.py", title="Calculate-AI", icon=":material/analytics:")

pg = st.navigation([home, calc, ai])
pg.run()
