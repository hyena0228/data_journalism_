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
st.header("같은 비 다른 느낌")
st.subheader("대한민국은 안전한 나라인가?")
st.write("""
2014년. 목포 팽목항은 아이들을 사회가 안전히 지켜내지 못했다는 죄책감이 짙게 드리워지고, 자녀들을 잃은 부모들의 절규로 가득 차 있었다. 이 무거운 감정은 전국으로 퍼져, 오래 동안 우리의 마음 속에 자리잡았다. 당시 국민의 안전과 재난관리를 책임지겠다며 ‘국민안전처’가 신설될 정도로 정부 역시 ‘안전’에 집중한 모습을 보였다. 대한민국 사회는 한 순간에 무고한 목숨을 앗아갈 수 있는 사고를 막고자 ‘안전’에 민감한 사회로 체질 변화를 꾀했다. 이러한 공감대 하에서 코로나19가 유행할 때도 동선 공개, 셧다운 등 강력한 제재를 바탕으로 국민의 안전을 책임지는 정책을 펼칠 수 있었다.
""")
st.write("")
col1, col2 = st.columns(2)

with col1:
   st.image("국민안전처.png")

with col2:
   st.image("행정안전부.png")

st.write("그러나 올 10월, 꽃피지 못한 수많은 청춘들을 허무하게 떠나보낸 충격적인 사고가 발생했다. 경찰 신고에도 적절한 조치가 없었다는 정황이 속속 드러남에 따라 과연 우리나라가 안전한지 다시 한번 반성과 질책의 목소리가 높아지고 있다.")

st.write("")
st.write("")
st.subheader("이상기후, 국민들의 안전을 위협하다")
st.write("이상기후로 안전이 위협되는 경우도 늘고 있다. 특히 이번 여름, 폭우로 인해 전국 곳곳이 홍역을 치렀다. 지난 8월에는 한반도에 오래 머무른 장마전선으로 인해 중부 지역이 모두 초토화됐다. 강원도나 충청지역에 산사태 사고가 잇따랐고 서울도 115년만에 폭우로 건물과 도로가 물에 잠겼다. 9월에는 강한 태풍이 남부지방을 지나며 경주와 포항이 피해 입은 바가 있다.")
st.image("포항피해.png")
st.write("특히나 8월의 서울 폭우 피해와 9월의 포항 태풍 피해는 한동안 대한민국에서 제일 뜨거운 이슈였다. 반지하에 살던 장애인 가족이 침수로 인해 목숨을 잃고, 지하주차장이 침수되어 차를 옮기러 갔던 입주민들이 사망하는 등 인명피해 사고가 발생했기 때문이다.")
st.image("서울피해.png")
##서울공화국
st.write("")
st.write("")
st.subheader("서울공화국")

st.write("같은 폭우 피해인 포항과 서울. 우리는 이 둘을 어떻게 받아들였을까?")
st.write("아래 자료는 서울과 포항의 폭우 피해 이후 뉴스 기사 댓글로 워드클라우드 작업을 한 결과다.")

st.write("⦁ 서울 기사 댓글")
from PIL import Image
s_comment = Image.open('서울댓글.png')
st.image(s_comment, caption="'서울 호우'를 키워드로 검색한 기사의 댓글 워드클라우드")
st.info(
"""
💡 네이버 뉴스에서 ‘서울 폭우’라는 키워드로 검색해 나온 2022년 8월 8일부터 8월 31일까지의 기사 댓글에서 수집함. 각 날짜 별로 3페이지씩 크롤링 진행하였으며 편향을 막기위하여 기사당 최대 20개의 댓글을 수집함. 총 댓글 수는 211개.
""", 
)
keyword = st.radio(
    "자세한 키워드 설명",
    ('뭐', '국민', '이돈', '정치인'))

if keyword == '뭐':
    st.write("'세후니 뭐하는겨?', '백날 책상에 앉아서 서류만 보면 뭐합니까~', '공무원들 뭐 했냐?', 'ㅡㅐ통령이나 국회의원이나 청장이나 시장이나 똑같지뭐ㅋㅋ' 등 부정적인 맥락의 댓글에서 주로 등장. ")
elif keyword == '국민':
    st.write("서울시에서 일어난 일에 관한 기사임에도 댓글에서 시민보다 국민이 더 큰 비중을 차지한 것이 인상적.") 
elif keyword == '이돈':
    st.write("오세훈 시장을 오세이돈으로 지칭해 등장한 키워드. 오세훈 시장이 물난리를 몰고 다닌다는 의미에서 붙여진 별칭.")  
elif keyword == '정치인':
    st.write("'대통령', '시장', '공무원', '오세훈', '윤' 등 정치인 관련 키워드들이 눈에 띔.")     



st.write("⦁ 포항 기사 댓글")

s_comment = Image.open('포항댓글.png')
st.image(s_comment, caption="'포항 폭우'를 키워드로 검색한 기사의 댓글 워드클라우드")
st.info(
"""
💡 네이버 뉴스에서 ‘포항 폭우’라는 키워드로 검색해 나온 2022년 9월 6일부터 9월 29일까지(서울과 똑같은 기간)의 기사 댓글에서 수집함. 각 날짜 별로 3페이지씩 크롤링 진행하였으며 편향을 막기위하여 기사당 최대 20개의 댓글을 수집함. 총 댓글 수는 117개.
""", 
)





##안전권 정의
st.write("")
st.write("")
st.subheader("안전권이란?")
st.write("안전권이란 국민이 각종 위험으로부터 안전을 보호받을 권리이다. 헌법 제34조 6항에 의하면 '국가는 재해를 예방하고 그 위험으로부터 국민을 보호하기 위하여 노력하여야 한다.'라고 규정하고 있다. 이는 국가가 재해 예방에 대한 의무를 지니고 있으며, 국민의 안전권을 보장해야 함을 명시한 것이다.")
st.image("안전.png")
st.write("재난 발생은 ‘평상시의 대비책 -> 재난 발생 -> 피해 발생 -> 사건 이해 -> 원인 분석 -> 재발 방지 대책’의 과정으로 흘러간다. 만일 이 사이클에서 서울과 포항의 차이가 있다면 안전권 차이가 있다는 것이다. 이미 사건을 이해하는 정도에서 차이를 확인했기에 더욱 세밀한 분석이 필요하다. 포항과 서울의 홍수 피해가 어떻게 다르게 다루어지고 있는지 배수, 교육 등의 대비책에서 시작하여 사건에 대한 주목도, 투입된 재정 규모 등으로 확인하고자 한다.")

##서울, 포항 폭우 및 태풍 피해 짚고 넘어가기
st.write("")
st.write("")
st.subheader("서울, 포항 폭우 및 태풍 피해 짚고 넘어가기")
st.write("본격적인 논의에 앞서 서울과 포항의 기본 정보부터 올 여름의 폭우 정보를 살펴보자.")
st.image("올여름 인포.png")
st.write("서울이 인구수는 19배 많지만 포항은 면적이 약 2배 가까이 넓다. 올 여름 피해 시의 강수량도 포항이 더 많았다. 인명피해는 포항의 사망자가 1명 더 많았으며, 이재민은 서울이 1600여명, 포항은 760여명이었다. 주목할 점은 재산피해 규모다. 포항은 제철소 및 원자력발전소 등 주요 시설이 위치해 있어서 약 25배 많은 재산피해가 발생했다.")




#올 여름 서울과 포항 호우 관련 데이터 확인
#rain_2022 = load_excel("2022 강수.xlsx")


#rain_2022 = pd.DataFrame({"서울": [1770], "포항": [1055]})
#rain_2022.index = ["2022년 일일강수량 합"]
#rain_2022.columns = []
#st.bar_chart(rain_2022, height = 500, width=500)





##서울, 포항 얼마만큼 집중호우에 준비해왔는가?
st.write("")
st.write("")
st.subheader("서울, 포항 얼마만큼 집중호우에 준비해왔는가?")

#서울-포항 호우 데이터

st.write("그렇다면 평상시 서울과 포항은 집중호우에 어떻게 대비해왔을까?")
ur = load_csv("usual_rain.csv")

ur_mean = ur[["장마 기간 중 합계강수량 평균"]]
ur_mean.index = ["서울", "포항"]
ur_mean.columns = ["장마 기간 중 평균 합계강수량"]

st.bar_chart(ur_mean, height = 250, use_container_width=True)

ur_max = ur[["장마 기간 중 합계강수량 최대"]]
ur_max.index = ["서울", "포항"]
ur_max.columns = ["장마 기간 중 최대 합계강수량"]

st.bar_chart(ur_max, height = 250, use_container_width=True)
st.write("장마기간 중 비가 많이 오는 곳은 서울이다. 서울은 1068.4mm의 최대 합계강수량과  431mm의 평균 합계강수량을 보이지만 포항은 각각 591mm, 249mm을 기록했다.")

day_max = ur[["일일 강수량 1st"]]
day_max.index = ["서울", "포항"]
day_max.columns = ["최대 일일강수량"]

st.bar_chart(day_max, height = 250, use_container_width=True)
st.write("그러나 포항은 한번 비가 올 때, 많이 오는 편이었다. 같은 기간의 최대 일일강수량은 포항이342mm, 서울이 176mm였다. 한번에 많은 비가 내리기에 포항은 배수 시설이 그 만큼 중요하다.")







#배수데이터

st.write("⦁ 서울과 포항 배수 데이터")

bpbp = pd.DataFrame(data = [31713.8, 9793], index = ["서울", "포항"], columns = ["배수장 최대배수량"]) #csv 파일에서 숫자만 뽑아왔습니다

st.bar_chart(bpbp, height = 500, use_container_width=True)

bs = pd.DataFrame(data = [2254620, 99813], index = ["서울", "포항"], columns = ["배수지 시설용량"])
st.bar_chart(bs, height = 500, use_container_width=True)




##언론에서의 차이
st.write("")
st.write("")
st.subheader("언론에서의 차이")

from PIL import Image
s_head = Image.open('서울폭우연관어분석_20221125.png')

st.image(s_head, caption="'서울 호우'를 포함하는 헤드라인 워드클라우드")

p_head = Image.open('포항폭우연관어분석_20221126.png')
st.image(p_head, caption="'포항 폭우'를 포함하는 헤드라인 워드클라우드")



##재발 방지 대책 및 수습 정책에서의 차이
st.write("")
st.write("")
st.subheader("재발 방지 대책 및 수습 정책에서의 차이")