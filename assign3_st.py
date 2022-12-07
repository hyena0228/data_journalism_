import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import seaborn as sb
import altair as alt



st.title("Streamlit으로 보는 타익타닉 데이터")
#Q1
st.subheader("타이타닉 생존자와 사망자 성별로 나누어 보기")

@st.cache
def load_data(filename):
    data = pd.read_excel(filename)
    return data

df = load_data("titanic3.xls")

female_survived_number = 0
female_perished_number = 0
female_survived = (df['sex'] == 'female') & (df['survived'] == True)
female_survived_number = female_survived.value_counts()[1] 
female_perished = (df['sex'] == 'female') & (df['survived'] == False)
female_perished_number = female_perished.value_counts()[1] 

male_survived_number = 0
male_perished_number = 0
male_survived = (df['sex'] == 'male') & (df['survived'] == True)
male_survived_number = male_survived.value_counts()[1] 
male_perished = (df['sex'] == 'male') & (df['survived'] == False)
male_perished_number = male_perished.value_counts()[1] 

df_sex = pd.DataFrame(data=np.array([[male_survived_number, female_survived_number], [male_perished_number,female_perished_number]]), index = ['survived', 'perished'], columns = ['male', 'female'])

st.bar_chart(df_sex, width = 25, use_container_width=True)

#Q2
st.subheader("생존자와 사망자의 평균 티켓 가격 보기")
people_survived = df[df['survived'] == True]
people_survived.fare.mean()

people_perished = df[df['survived'] == False]
people_perished.fare.mean()

df_fare = pd.DataFrame(data=np.array([people_survived.fare.mean(), people_perished.fare.mean()]), index = ['survived', 'perished'],
columns = ['fare_mean'])
st.bar_chart(df_fare, width = 0, use_container_width=True)


#Q3
st.subheader("성별에 따른 데이터 프레임")
st.write(df_sex)

#Q4
st.subheader("생존자와 사망자 Pclass로 나누어보기")

pclass_1_survived = (df['pclass'] == 1) & (df['survived'] == True)
pclass_1_perished = (df['pclass'] == 1) & (df['survived'] == False)
pclass_2_survived = (df['pclass'] == 2) & (df['survived'] == True)
pclass_2_perished = (df['pclass'] == 2) & (df['survived'] == False)
pclass_3_survived = (df['pclass'] == 3) & (df['survived'] == True)
pclass_3_perished = (df['pclass'] == 3) & (df['survived'] == False)

pclass_1_sur_num = pclass_1_survived.value_counts()[1]
pclass_1_per_num = pclass_1_perished.value_counts()[1]
pclass_1_total = pclass_1_sur_num + pclass_1_per_num
pclass_2_sur_num = pclass_2_survived.value_counts()[1]
pclass_2_per_num = pclass_2_perished.value_counts()[1]
pclass_2_total = pclass_2_sur_num + pclass_2_per_num
pclass_3_sur_num = pclass_3_survived.value_counts()[1]
pclass_3_per_num = pclass_3_perished.value_counts()[1]
pclass_3_total = pclass_3_sur_num + pclass_3_per_num

df_pclass = pd.DataFrame(data=np.array([[pclass_1_sur_num, pclass_1_per_num], [pclass_2_sur_num, pclass_2_per_num], [pclass_3_sur_num, pclass_3_per_num ]]), 
index = ['pclass1', 'pclass2', 'pclass3'], columns = ['survived', 'perished'])

st.area_chart(df_pclass)

#Q5
st.subheader("동반자 수에 따른 생존률 보기")
sibsp_0_sur = (df['sibsp'] == 0) & (df['survived'] == True)
sibsp_0_per = (df['sibsp'] == 0) & (df['survived'] == False)
sibsp_1_sur = (df['sibsp'] == 1) & (df['survived'] == True)
sibsp_1_per = (df['sibsp'] == 1) & (df['survived'] == False)
sibsp_more2_sur = (df['sibsp'] >= 2) & (df['survived'] == True)
sibsp_more2_per = (df['sibsp'] >= 2) & (df['survived'] == False)

sibsp_0_sur_num = sibsp_0_sur.value_counts()[1]
sibsp_0_per_num = sibsp_0_per.value_counts()[1]
sibsp_1_sur_num = sibsp_1_sur.value_counts()[1]
sibsp_1_per_num = sibsp_1_per.value_counts()[1]
sibsp_more2_sur_num = sibsp_more2_sur.value_counts()[1]
sibsp_more2_per_num = sibsp_more2_per.value_counts()[1]

df_sibsp = pd.DataFrame(data=np.array([sibsp_0_sur_num / (sibsp_0_sur_num + sibsp_0_per_num), sibsp_1_sur_num / (sibsp_1_sur_num + sibsp_1_per_num), 
sibsp_more2_sur_num / (sibsp_more2_sur_num + sibsp_more2_per_num)]), 
index = ['sibsp=0', 'sibsp=1', 'sibsp>=2'], columns = ['survived rate'])

st.line_chart(df_sibsp)