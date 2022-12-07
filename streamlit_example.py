import streamlit as st
import pandas as pd
import numpy as np

# Webpage Title
st.title("Streamlit으로 만드는 데이터 앱")

st.header("Streamlit이란?")

st.write("Streamlit은 데이터분석 결과를 가장 빠르게 웹기반 리포트를 작성하고 공유할 수 있는 플랫폼이다.")
st.write("간단한 파이썬 코드를 이용해 데이터기반 홈페이지를 손쉽게 만들 수 있다. 현재 깃허브(github)에서 가장 인기있는 프로젝트중 하나이며 정보시각화(visualization)을 손쉽게 포함시킬 수 있다.")

st.info(
"""
참고자료
* API Document: https://docs.streamlit.io/library/api-reference
* Examples: https://github.com/MarcSkovMadsen/awesome-streamlit
"""
)

st.subheader("Streamlit 설치")
st.code("pip install streamlit")

st.subheader("Streamlit 실행")
st.code("python run tutorial.py")

st.header("인터페이스 위젯 만들기")

st.subheader("텍스트 입력")
st.write("텍스트의 입력은 `st.write()` 함수를 사용한다.")

st.subheader("Markdown")
st.markdown(
"""
Markdown 문법으로 텍스트를 입력하려면 `st.markdown()`을 사용한다. Markdown에서 활용가능한 모든 문법을 사용할 수 있다.

예를 들어,
* bullet point1
* bullet point2
    * bullet point2-1
를 입력하거나,
1. 숫자항목 1 
2. 숫자항목 2
를 입력할 수 있다.

## 헤딩 2
### 헤딩 3
과 같이 제목을 입력하거나,
> block quote 
의 입력도 가능하다.

수평선을 만들기 위해서는 `- - -` 혹은  `***` 등을 입력한다.
- - -
***

링크를 만들기 위해서는 다음과 같이.
[googlelink]: https://google.com "Go google"

테이블의 추가도 가능하다.
|          | male | female |
|----------|------|--------|
| Survived |  0   |     2  |
| Deceased |      |        |

"""
)

st.markdown("***")

st.subheader("버튼 만들기")
if st.button("버튼을 눌러주세요"):
      st.write("데이터가 로딩 중입니다..")
      # 데이터 로딩 함수는 여기에!

st.subheader("체크박스 만들기")
cb1 = st.checkbox('체크박스 1')	
if cb1:
    st.write('체크박스 1을 선택했어요.')
cb2 = st.checkbox('체크박스 2', value=True)
if cb2:
    st.write('체크박스 2는 default로 선택이 되었습니다.')

st.subheader("라디오 버튼 만들기")
selected_item = st.radio("Radio Part", ("A", "B", "C"))	
if selected_item == "A":
    st.write("A가 선택됨")
elif selected_item == "B":
    st.write("B가 선택됨")
elif selected_item == "C":
    st.write("C가 선택됨")

st.subheader("선택 박스 만들기")
option = st.selectbox('Please select in selectbox!',
                     ('Americano', 'Café Latte', 'Café Mocha'))	
st.write('You selected:', option)

st.subheader("다중 선택 박스 만들기")
multi_select = st.multiselect('Please select somethings in multi selectbox!',
                             ['Americano', 'Café Latte', 'Café Mocha', 'Tea'])
st.write('You selected:', multi_select)
st.write('결과를 list 형태로 반환한다.')

st.subheader("슬라이더 만들기")
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


st.markdown("***")

st.header("데이터 입력")

st.subheader("텍스트 데이터의 입력")
title = st.text_input("type anything")
st.write('The current movie title is', title)

st.subheader("날짜 데이터의 입력")
dt = st.date_input("type your date")
st.write('The date is', dt)

st.markdown("***")

st.header("데이터 출력")

st.subheader("")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write("Interactive Table")
st.dataframe(df) # same as df or st.write(df)

st.write("Interactive Table with Highlight")
st.dataframe(df.style.highlight_max(axis=0))

st.write("Static Table")
st.table(df)

st.markdown("***")

st.header("시각화 예제")

st.subheader("Vega-Light")

st.info("https://vega.github.io/vega-lite/")

df_vega = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

st.vega_lite_chart(df_vega, {
    'width': 'container',
    'height': 500,
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
         'x': {'field': 'a', 'type': 'quantitative'},
         'y': {'field': 'b', 'type': 'quantitative'},
         'size': {'field': 'c', 'type': 'quantitative'},
         'color': {'field': 'c', 'type': 'quantitative'},
    },
}, use_container_width=True)

st.subheader("Plotly")

st.info("https://plotly.com/python/")

import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)


import plotly.express as px

gm_df = px.data.gapminder()
years = gm_df.year.unique()
target_year = st.slider('Select a year:', min_value=int(years.min()), max_value=int(years.max()), step=5)
fig3 = px.scatter(gm_df.query("year=={}".format(target_year)), x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)
st.plotly_chart(fig3, use_container_width=True)