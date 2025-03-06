import streamlit as st

cart_button = st.button("Add to cart", key="cart_button",
                        icon=":material/shopping_cart:")

if cart_button:
    st.write("Added to cart!")

home = st.Page("home.py", title="Home", icon=":material/home:")

calc = st.Page("calc.py", title="Calculate-Operating",
               icon=":material/calculate:")

ai = st.Page("ai.py", title="Calculate-AI", icon=":material/analytics:")

pg = st.navigation([home, calc, ai])
pg.run()
