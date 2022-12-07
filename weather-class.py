import streamlit as st
import pandas as pd
import numpy as np

    data = pd.read_csv(filename)
    data.date = pd.to_datetime(data.date)
    return data

# 데이터 로딩
# df = pd.read_csv("weather-mod.csv") ## 일반적인 방법
df = load_data("weather-mod.csv") ## st.cache를 이용하는 방법

# 홈페이지 타이틀과 설명
st.title("날씨 데이터 분석")
st.write(
    "앞의 강의에서 살펴본 날씨 데이터를 이용하여 데이터를 필터링하고 그래프를 그려보았다. \
    먼저 분석에 사용한 전체 데이터는 다음과 같다. 데이터를 살펴보려면 아래의 <전체 데이터 보기> 버튼을 눌러보자."
)

# 데이터 테이블 보기. 
# 테이블을 홈페이지 로딩된 후 바로 보여주지 않고 <전체 데이터 보기> 버튼을 눌렀을 때 보여준다.
if st.button("전체 데이터 보기"):
    st.write("### 데이터")
    st.write("전체 데이터는 2012년 3월 10일 부터 2013년 3월 10일 까지 매일의 날씨를 기록하고 있다.")
    st.write(pd.DataFrame(df))

    # st.expander는 접고 펼칠 수 있는 박스를 그려준다.
    with st.expander("데이터 설명"):
        # st.code는 code형식의 데이터를 보여줄 때 사용된다. language='' 옵션을 사용하면 해당 언어에 맞게 칼라코딩을 해준다.
        st.code(
            """max_temp : 최고 기온 (˚F) \nmean_temp : 평균 기온 (˚F) \nmin_temp : 최저 기온 (˚F) \nevents : 날씨를 Rain, Snow, Fog, Thunderstorm 으로 기록
            """
        )

# Markdown 문법을 사용하기 위한 함수
st.markdown("<hr>", unsafe_allow_html=True)

# Radio Button 사용 예
st.markdown("### 날씨 이벤트 선택 (Radio Button)")
st.write(
    """
    데이터는 매일의 날씨 이벤트를 "Rain", "Thunderstorm", "Fog", "Snow"의 네가지로 기록하고 있다.
    아래의 라디오 버튼을 눌러 이벤트가 포함된 날짜를 확인해보자.
    """
)
