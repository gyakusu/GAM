# In[0]:

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

data_df = pd.read_csv('data/bearings.csv')
show_df = data_df.copy()
def get_colors(n): return sns.color_palette("husl", n).as_hex()

# In[0]:


st.title('NSK Bearing Selector')
st.write('NSK-AI will select the optimal bearing for you.')

left_column, middle_column, right_column = st.columns(3)

radio_buttonL = left_column.radio('Choose your application', [
    None, 'Automotive', 'Machine tools', 'Wind turbine'])

if radio_buttonL:
    if radio_buttonL == 'Automotive':
        left_column.radio('Choose your Automotive', [
            'Gear Box', 'Engine', 'Wheel'])

    elif radio_buttonL == 'Machine tools':
        left_column.radio('Choose your Machine tools', [
            'Lathe', 'Milling machine', 'Grinding machine'])

    else:
        left_column.radio('Choose your Wind turbine',
                          ['Gear Box', 'Generator'])

Dim_typeM = ['Inner Diameter, d [mm]',
             'Outer Diameter, D [mm]', 'Width, W [mm]']
radio_buttonM = middle_column.radio('Choose your Dimension', Dim_typeM)
dim_valueM = middle_column.text_input(radio_buttonM, '10')
buttonM = middle_column.button(f'Set {radio_buttonM}')
another_type = [x for x in Dim_typeM if x != radio_buttonM]

if 'radio_buttonM1' not in st.session_state:
    st.session_state.radio_buttonM1 = None
if 'radio_buttonM2' not in st.session_state:
    st.session_state.radio_buttonM2 = None
if 'buttonM2' not in st.session_state:
    st.session_state.buttonM2 = False

if buttonM:
    if dim_valueM != '10':
        st.write(f'{radio_buttonM}: {dim_valueM} is not available.')
        st.stop()

    st.session_state.radio_buttonM1 = another_type[0]  # 初期値を設定

radio_buttonM1 = middle_column.radio(
    f'Choose remaining dimension', another_type, key='radio_buttonM1')

if radio_buttonM1:

    if radio_buttonM1 == another_type[0]:
        radio_buttonM2 = middle_column.radio(f'set {another_type[0]}', [
            '14', '28', '30', '32'], key='radio_buttonM2')
        buttonM2 = middle_column.button(
            f'Set {another_type[0]}', key='buttonM2')

        if buttonM2:
            show_df = data_df[data_df[another_type[0][-6:]]
                              == int(radio_buttonM2)]

    elif radio_buttonM1 == another_type[1]:
        radio_buttonM2 = middle_column.radio(f'set {another_type[1]}', [
            '8', '9', '10', 14], key='radio_buttonM2')
        buttonM2 = middle_column.button(
            f'Set {another_type[1]}', key='buttonM2')

textR = right_column.text_input('Rotational speed [r/min]', '1000')

st.subheader('You might like this')
st.write('Service Life, L [h] and Torque, T [Nm] are estimated by NSK-AI.')

st.data_editor(
    show_df,
    column_config={
        "favorite": st.column_config.CheckboxColumn(
            " ",
            default=False,
        )
    },
    disabled=["widgets"],
    hide_index=True,
)

df1 = show_df[['Bearing', 'Recommendation', 'Sales_volume']].copy()

fig0 = px.bar(df1,
              x='Sales_volume',
              y='Bearing',
              title='Sales volume of bearings',
              orientation='h',
              color=get_colors(len(df1)))
fig0.update_layout(showlegend=False)

fig1 = px.pie(df1, values='Recommendation', names='Bearing',
              title='Degree of our recommendation')

fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.plotly_chart(fig0)

with fig_col2:
    st.plotly_chart(fig1)


col1, col2 = st.columns(2)

with col1:
    if st.button('Calculate Operation'):
        st.switch_page('calc.py')

with col2:
    if st.button('Calculate With AI'):
        st.switch_page('ai.py')
