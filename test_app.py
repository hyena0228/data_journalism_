#pip install streamlit


import pandas as pd
import numpy as np
import streamlit as st

st.title("Streamlit으로 만드는 데이터앱") #타이틀 만들기
st.header("Streamlit이란?")
st.write("~~~~~")
st.info("""
참고자료
*
*
""")

st.subheader("Streamlit 설치")
st.code(
"""
pip install streamlit
conda install streamlit
"""
)

st.header("인터페이스 위젯만들기")

st.subheader("텍스트 입력")
st.write("텍스트의 입력은 `st.write()`함수를 사용한다") # ``
