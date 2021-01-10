import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit')

"""
## プログレスバー
"""
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i+1)
#     time.sleep(0.1)


"""
## expander
"""
expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')

expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答')

expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

"""
## レイアウト変更（2カラムの例）
"""
left_column, right_column = st.beta_columns(2)
button = left_column.button('left column')
if button:
    right_column.write('test')

"""
## インタラクティブ ウィジェット
"""
# チェックボックス
if st.sidebar.checkbox('Show Image'):
    img2 = Image.open('./frontale.jpeg')
    st.image(img2, caption='frontale', use_column_width=True)

# セレクトボックス
option = st.sidebar.selectbox(
    '数字を入力',
    options=list(range(1, 10))
)
'選択した数字は', option, 'です。'

# テキストボックス
text = st.text_input('文字を入力')
'入力した文字は', text, 'です。'

# スライダー
condition = st.slider('今の調子は？',0, 100, 50)
'コンディション：', condition


"""
## 画像を表示
"""
img = Image.open('./frontale.jpeg')
st.image(img, caption='frontale', use_column_width=True)

"""
## マップのプロット
"""
df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)

"""
## チャートを描く
"""
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

"""
## データフレームを表示
"""

df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})
st.write('write')
st.write(df)
st.write('dataframe')
st.dataframe(df.style.highlight_max(axis=0), width=200, height=300)
st.write('table')
st.table(df)

"""
マジックコマンド
# 章
## 節
### 項
---
"""