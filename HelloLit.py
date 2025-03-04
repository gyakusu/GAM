import streamlit as st
import pandas as pd

st.title('NSK Bearing Selector')
st.write('NSK-AI will select the optimal bearing for you.')

# 3つの欄を横に並べる
left_column, middle_column, right_column = st.columns(3)

# ラジオボタン'Car', 'Machine tools', 'Wind turbine'を選択させる
radio_buttonL = left_column.radio('Choose your application (optional)', [None, 'Car', 'Machine tools', 'Wind turbine'])

# ラジオボタンが変更された場合に、次のラジオボタンを表示
if radio_buttonL:
    if radio_buttonL == 'Car':
        left_column.radio('Choose your Car', ['Gear', 'Tyre', 'Engine'])

    elif radio_buttonL == 'Machine tools':
        left_column.radio('Choose your Machine tools', ['Lathe', 'Milling machine', 'Grinding machine'])
        
    else:
        left_column.radio('Choose your Wind turbine', ['Onshore', 'Offshore'])

# 横並びのラジオボタンでInner Diameter, Outer Diameter, Widthを選択させる
Dim_typeM = ['Inner Diameter, d', 'Outer Diameter, D', 'Width, W']
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

radio_buttonM1 = middle_column.radio(f'Choose remaining dimension', another_type, key='radio_buttonM1')

if radio_buttonM1:
    if radio_buttonM1 == another_type[0]:
        radio_buttonM2 = middle_column.radio(f'set {another_type[0]}', ['19', '22', '26'], key='radio_buttonM2')
        buttonM2 = middle_column.button(f'Set {another_type[0]}', key='buttonM2')
    elif radio_buttonM1 == another_type[1]:
        radio_buttonM2 = middle_column.radio(f'set {another_type[1]}', ['5', '6', '8'], key='radio_buttonM2')
        buttonM2 = middle_column.button(f'Set {another_type[1]}', key='buttonM2')

textR0 = right_column.text_input('Radial force, Fr [kN]', '0')
textR1 = right_column.text_input('Axial force, Fa [kN]', '10')
textR2 = right_column.text_input('Rotational speed [r/min]', '1000')
textR3 = right_column.text_input('Operating temperature [°C]', '20')

st.subheader('You might like this')
st.write('Life, L [h] and Torque, T [Nm] are estimated by NSK-AI.')

df0 = pd.DataFrame({
    'L [h] (est)': ['10000', '20000', '30000'],
    'T [Nm] (est)': ['0.01', '0.02', '0.03'],
    'Bearing': ['6200', '6300', '6400'],
    'type': ['Ball', 'Ball', 'Cylindrical'],
    'd [mm]': ['10', '10', '10'],
    'D [mm]': ['30', '35', '40'],
    'W [mm]': ['9', '11', '12'],
    'Limiting [rpm]': ['26000', '22000', '19000'],
})

st.write(df0)

button0 = st.button('Next')




