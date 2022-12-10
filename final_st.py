import streamlit as st
import pandas as pd
import numpy as np

import altair as alt




import json
from pprint import pprint



import openpyxl
import sklearn


@st.cache(allow_output_mutation=True)
def load_excel(filename):
    data = pd.read_excel(filename)
    return data


@st.cache
def load_csv(filename):
    data = pd.read_csv(filename)
    return data

st.subheader("대한민국은 안전한 나라인가?")
st.write("⦁ 2014년 이후 안전에 민감해진 대한민국")

st.subheader("이상기후, 국민들의 안전을 위협하다")
st.write("⦁ 지난 여름 서울과 포항에 물난리가 덮쳤다.")
st.write("⦁ 각각 8월, 9월 초 뉴스 헤드라인을 뜨겁게 달궜다.")


##서울공화국
st.subheader("서울공화국")
st.write("같은 폭우 피해, 우리는 이를 어떻게 받아들였을까?")

st.write("⦁ 서울 기사 댓글")
from PIL import Image
s_comment = Image.open('서울댓글.png')
st.image(s_comment, caption="'서울 호우'를 키워드로 검색한 기사의 댓글 워드클라우드")
st.info(
"""
💡 네이버 뉴스에서 ‘서울 폭우’라는 키워드로 검색해 나온 2022년 8월 8일부터 8월 31일까지의 기사 댓글에서 수집함. 각 날짜 별로 3페이지씩 크롤링 진행하였으며 편향을 막기위하여 기사당 최대 20개의 댓글을 수집함. 총 댓글 수는 211개.
""", 
)


st.write("⦁ 포항 기사 댓글")
from PIL import Image
s_comment = Image.open('포항댓글.png')
st.image(s_comment, caption="'포항 폭우'를 키워드로 검색한 기사의 댓글 워드클라우드")
st.info(
"""
💡 네이버 뉴스에서 ‘포항 폭우’라는 키워드로 검색해 나온 2022년 9월 6일부터 9월 29일까지(서울과 똑같은 기간)의 기사 댓글에서 수집함. 각 날짜 별로 3페이지씩 크롤링 진행하였으며 편향을 막기위하여 기사당 최대 20개의 댓글을 수집함. 총 댓글 수는 117개.
""", 
)



json_data = []
with open("comments.json", encoding = 'UTF-8') as file:
    data = json.load(file)
        
json.dumps(data)
#print(data[0]["comment"])
#print(len(data))

total_text = ""
for i in range(len(data)):
    if data[i]['comment']:
        total_text = total_text + " " + data[i]['comment'].strip()




#okt = Okt()



##안전권 정의
st.subheader("안전권 정의")

##서울, 포항 폭우 및 태풍 피해 짚고 넘어가기
st.subheader("서울, 포항 폭우 및 태풍 피해 짚고 넘어가기")




#인구밀도 등 기본데이터 확인
st.write("⦁ 두 도시는 얼마만큼 다른가?")

city = load_excel("시별 정보.xlsx")


st.table(city)

#침수 피해 데이터
st.write("⦁ 침수 피해 데이터")
harm = load_excel("서울 포항 피해데이터.xlsx")
harm = harm[["내용", "사망자", "이재민(명)", "주택/상가 침수(동)", "총 피해액(백만)"]]
harm.set_index('내용', inplace=True)
st.table(harm)

#올 여름 서울과 포항 호우 관련 데이터 확인
rain_2022 = load_excel("2022 강수.xlsx")


rain_2022 = pd.DataFrame({"서울": [1770], "포항": [1055]})
rain_2022.index = ["2022년 일일강수량 합"]
#rain_2022.columns = []
st.bar_chart(rain_2022, height = 500, width=500)





##서울, 포항 얼마만큼 집중호우에 준비해왔는가?
st.subheader("서울, 포항 얼마만큼 집중호우에 준비해왔는가?")

#서울-포항 호우 데이터

st.write("⦁ 장마기간 서울과 포항 호우 데이터")
ur = load_csv("usual_rain.csv")
day_max = ur[["일일 강수량 1st"]]
day_max.index = ["서울", "포항"]
day_max.columns = ["최대 일일강수량"]

st.bar_chart(day_max, height = 250, use_container_width=True)

ur_max = ur[["장마 기간 중 합계강수량 최대"]]
ur_max.index = ["서울", "포항"]
ur_max.columns = ["장마 기간 중 최대 합계강수량"]

st.bar_chart(ur_max, height = 250, use_container_width=True)

ur_mean = ur[["장마 기간 중 합계강수량 평균"]]
ur_mean.index = ["서울", "포항"]
ur_mean.columns = ["장마 기간 중 평균 합계강수량"]

st.bar_chart(ur_mean, height = 250, use_container_width=True)






#배수데이터

st.write("⦁ 서울과 포항 배수 데이터")
SeoulBaesuPump = pd.read_csv("SeoulBaesuPump.csv", encoding='cp949')

SBP_main = SeoulBaesuPump[["시설관리자", "배수장_최대배수량"]]
SBP_main = SBP_main.groupby('시설관리자').sum('배수장_최대배수량')
SBP_main = SBP_main.sort_values('배수장_최대배수량')
#st.write(SBP_main.sort_values('배수장_최대배수량'))



PohangBaesuPump = pd.read_csv("PohangBaesuPump.csv", encoding='cp949')
PBP_main = PohangBaesuPump[['시군', '처리능력']]
PBP_main = PBP_main.groupby('시군').sum('처리능력')
PBP_main.columns = ["배수장_최대배수량"]

bp_result = pd.concat([SBP_main, PBP_main])

st.bar_chart(bp_result, height = 500, use_container_width=True)

SeoulBaesu = pd.read_excel("SeoulBaesu.xlsx", thousands = ',')
SB_main = SeoulBaesu[['배수위치', '시설용량(㎥/일)']]
SB_main = SB_main.dropna(axis = 0)
SB_main['시설용량(㎥/일)'] = SB_main['시설용량(㎥/일)'].apply(pd.to_numeric)
SB_main = SB_main.groupby('배수위치').sum('시설용량(㎥/일)')
SB_main = SB_main.sort_values('시설용량(㎥/일)')




PohangBaesu = pd.read_excel("PohangBaesu.xlsx", thousands = ',')
PB_main = PohangBaesu[['배수위치', '시설용량(㎥/일)']]
PB_main = PB_main.dropna(axis = 0)
PB_main['시설용량(㎥/일)'] = PB_main['시설용량(㎥/일)'].apply(pd.to_numeric)
PB_main = PB_main.groupby('배수위치').sum('시설용량(㎥/일)')


b_result = pd.concat([SB_main, PB_main])
st.bar_chart(b_result, height = 500, use_container_width=True)



##언론에서의 차이
st.subheader("언론에서의 차이")

from PIL import Image
s_head = Image.open('서울폭우연관어분석_20221125.png')

st.image(s_head, caption="'서울 호우'를 포함하는 헤드라인 워드클라우드")

p_head = Image.open('포항폭우연관어분석_20221126.png')
st.image(p_head, caption="'포항 폭우'를 포함하는 헤드라인 워드클라우드")



##재발 방지 대책 및 수습 정책에서의 차이
st.subheader("재발 방지 대책 및 수습 정책에서의 차이")