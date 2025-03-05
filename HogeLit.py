import streamlit as st
import pandas as pd
import plotly.express as px

# サンプルデータを作成
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [30, 20, 40, 10]
}

# データフレームを作成
df = pd.DataFrame(data)

# Streamlitアプリの構築
st.title('円グラフの表示（Plotly使用）')
st.write('以下はpandasデータから生成された円グラフです：')

# 円グラフを作成
fig = px.pie(df, values='Values', names='Category',
             title='Category Distribution')

# 円グラフをStreamlitで表示
st.plotly_chart(fig)

# ボタンを追加して次のページに遷移
if st.button('次のページへ'):
    st.experimental_set_query_params(page="next")
