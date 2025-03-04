import streamlit as st
import pandas as pd

st.title('Hello Streamlit')
st.write('This is a simple example of Streamlit.')

# Load data
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})

# Show data
st.write('Data Frame:')
st.write(df)

# Show chart
st.write('Chart:')
st.line_chart(df)

# Use command below to run this script
# ```bash
# $ streamlit run HelloLit.py
# ```
