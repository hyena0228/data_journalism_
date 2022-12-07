import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import altair as alt
from bs4 import BeautifulSoup
from konlpy.tag import Kkma

from wordcloud import WordCloud
import json
from pprint import pprint

from konlpy.tag import Okt
from nltk import Text
from matplotlib import font_manager, rc

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

st.subheader("이상기후, 국민들의 안전을 위협하다")

##서울공화국
st.subheader("서울공화국")
st.write("같은 폭우 피해, 우리는 이를 어떻게 받아들였을까?")

st.write("⦁ 서울 기사 댓글")
from PIL import Image
s_comment = Image.open('서울댓글.png')
st.image(s_comment, caption="'서울 호우'를 키워드로 검색한 기사의 댓글 워드클라우드")

st.write("⦁ 포항 기사 댓글")
from PIL import Image
s_comment = Image.open('포항댓글.png')
st.image(s_comment, caption="'포항 폭우'를 키워드로 검색한 기사의 댓글 워드클라우드")



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


st.write("⦁ 침수 피해 데이터")
harm = load_excel("서울 포항 피해데이터.xlsx")
harm = harm[["내용", "사망자", "이재민(명)", "주택/상가 침수(동)", "총 피해액(백만)"]]
harm.set_index('내용', inplace=True)
st.table(harm)



st.write("⦁ 두 도시는 얼마만큼 다른가?")

city = load_excel("시별 정보.xlsx")

st.table(city)







##서울, 포항 얼마만큼 집중호우에 준비해왔는가?
st.subheader("서울, 포항 얼마만큼 집중호우에 준비해왔는가?")

#서울-포항 호우 데이터

st.write("⦁ 장마기간 서울과 포항 호우 데이터")
ur = load_csv("usual_rain.csv")
ur_main = ur[["장마 기간 중 합계강수량 평균", "장마 기간 중 합계강수량 최대", "일일 강수량 1st", "일일 강수량 2nd", "일일 강수량 3rd"]]
ur_main.index = ["서울", "포항"]

ur_main = ur_main.T

st.line_chart(ur_main, height = 500, use_container_width=True)





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