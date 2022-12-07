import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from bokeh.plotting import figure

# st.cache를 이용하여 데이터 로딩을 하는 함수
@st.cache
def load_data(filename):
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

selected_item = st.radio("날씨 이벤트 선택", ("Rain", "Thunderstorm", "Fog", "Snow"))	

if selected_item == "Rain":
    filtered_df = df[df.rain] #df.rain이 true인 값만 저장하는 변수
    st.write(pd.DataFrame(filtered_df))
    st.write("비가 오는 날은 총 {}일입니다.".format(len(filtered_df)))
elif selected_item == "Thunderstorm":
    filtered_df = df[df.thunderstorm]
    st.write(pd.DataFrame(filtered_df))
    st.write("뇌우가 있던 날은 총 {}일입니다.".format(len(filtered_df)))
elif selected_item == "Fog":
    filtered_df = df[df.fog]
    st.write(pd.DataFrame(filtered_df))
    st.write("안개가 낀 날은 총 {}일입니다.".format(len(filtered_df)))
elif selected_item == "Snow":
    filtered_df = df[df.snow]
    st.write(pd.DataFrame(filtered_df))
    st.write("눈이 오는 날은 총 {}일입니다.".format(len(filtered_df)))

# 다중선택(multiselect) 사용 예
st.markdown("### 날씨 이벤트 선택 (다중선택)")
st.write(
    """
    라디오 버튼을 이용한 이벤트의 선택은 한번에 하나씩만 가능했다. 여러개의 이벤트를 선택하기 위해서는 `multiselect`박스를 사용한다. 체크박스를 사용하는 것도 가능하다.
    """
)

multi_select = st.multiselect('다중선택 박스에서 이벤트를 선택하세요.', ['rain', 'thunderstorm', 'fog', 'snow'])

if multi_select:
    filtered_df = df[["date", "rain", "thunderstorm", "fog", "snow", "events"]]
    for i in multi_select:
        filtered_df = filtered_df[filtered_df[i]] #multiselect의 여러 개 중 두 개가 리스트 안에 들어옴. 그걸 이용해 filtered_df 새로 만듦
    st.write(pd.DataFrame(filtered_df))
    st.write("선택된 날씨 이벤트가 있는 날은 총 {}일입니다.".format(len(filtered_df)))
st.markdown("<hr>", unsafe_allow_html=True)

# st.line_chart를 이용한 라인그래프
st.markdown("### 라인그래프 그리기")
st.write(
    """
    streamlit은 기본적인 그래프 그리기 기능을 제공한다. `st.line_chart(_dataframe_)`함수는 라인그래프를 그려준다.  
    """
)

st.line_chart(df[["min_temp", "max_temp", "mean_temp"]])

st.write(
    """
    `st.line_chart(_dataframe_)`함수는 손쉽게 데이터를 시각화할 수는 있지만 기능의 제한이 있다. \
    만약 그래프를 세부내용을 좀더 다듬고 인터랙티브한 시각화결과물을 만들고 싶다면 `bokeh`, `vega_lite`, `plotly` 등과 같은 시각화 도구를 이용해보자. \
    `streamlit`은 파이썬에서 사용가능한 대부분의 시각화 도구를 지원한다.
    """
)

st.info('Chart Gallery: https://docs.streamlit.io/library/api-reference/charts')

# Bokeh를 이용하여 그린 라인 그래프
st.markdown("### Bokeh로 그린 라인 그래프")
fig1 = figure(
     title='기온변화 추이 그래프',
     x_axis_label='Days',
     y_axis_label='Temperature(˚F)')

fig1.line(df.index, df.max_temp, legend_label='최고기온(˚F)', line_width=1, line_color="blue")
fig1.line(df.index, df.min_temp, legend_label='최저기온(˚F)', line_width=1, line_color="green")
fig1.line(df.index, df.mean_temp, legend_label='평균기온(˚F)', line_width=1, line_color="red", line_dash="dotted") #dashed는 - - - -

st.bokeh_chart(fig1, use_container_width=True) #전체 width에 맞게 그려줌.

# Bokeh를 이용하여 그린 scatter plot
st.markdown("### Bokeh로 그린 변인들 간의 상관관계")
st.write(
    """
    Streamlit이 제공하는 다양한 웹인터페이스를 활용하여 인터랙티브한 그래프를 그릴 수 있다. 
    `st.selectbox`를 이용하여 선택할 수 있는 변수의 예를 제시하였다. Regression line의 포함 여부는 `st.checkbox`를 활용하였다.
    """
)

# st.columns 을 이용하여 3개의 컬럼을 만들고 콘트롤을 넣어주었다.
col1, col2, col3 = st.columns(3) #한 줄을 세 부분으로 나눠 나열

with col1:
    choice_x = st.selectbox('X 축의 값을 선택하세요.',
    ('mean_temp', 'mean_humidity', 'mean_visibility', 'mean_dew', 'mean_wind', 'cloud_cover'))
with col2:
    choice_y = st.selectbox('Y 축의 값을 선택하세요.',
    ('mean_temp', 'mean_humidity', 'mean_visibility', 'mean_dew', 'mean_wind', 'cloud_cover'))
with col3:
    reg_line = st.checkbox('Draw Regression Line')



# 리그레션 라인 (fit line)의 계산
par = np.polyfit(df[choice_x], df[choice_y], 1, full=True)
slope=par[0][0]
intercept=par[0][1]
y_predicted = [slope*i + intercept  for i in df[choice_x]]

# Bokeh를 이용하여 그린 산점도 그래프
fig2 = figure(width=500, height=500,
    x_axis_label=choice_x, #셀렉트 박스를 통해 선택된 게 레이블로 넘어감
    y_axis_label=choice_y)
fig2.circle(df[choice_x], df[choice_y], size=5, color="navy", alpha=0.5) #alpha는 투명도
if reg_line:
    fig2.line(df[choice_x],y_predicted,color='red',legend_label='y='+str(round(slope,2))+'x+'+str(round(intercept,2)))
st.bokeh_chart(fig2, use_container_width=True)

# Matplotlib으로 그린 산점도
#fig, axe = plt.subplots()
#axe.scatter(df[cloud_cover], df[mean_humidity], marker = "o")
#axe.set_title("Mean Temperature and Mean Humidity")
#st.pyplot(fig)

# Seaborn으로 그린 산점도
sub_data = df[['mean_temp', 'mean_humidity', 'mean_visibility', 'cloud_cover']]
st.pyplot(sb.pairplot(sub_data, kind="reg"))
