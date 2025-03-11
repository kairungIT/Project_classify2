import streamlit as st
import pandas as pd

st.header("การพยากรณ์โรคหัวใจล้มเหลว")
st.header("        ด้วยเทคนิคเหมืองข้อมูล        ")
st.header("              ")

c1,c2,c3=st.columns(3)
with c1:
        st.write("")
with c2:
        st.image('./img/heart1.jfif')
with c3:
        st.write("")

dt= pd.read_csv('./data/Heart3.csv')

st.header("ข้อมูลโรคหัวใจ")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลโรคหัวใจ")
st.write(dt.describe())
st.write("สถิติจำนวนเพศหญิง=0 เพศชาย=1")
st.write(dt.groupby('Sex')['Sex'].count())

count_male = dt.groupby('Sex').size()[1]
count_female = dt.groupby('Sex').size()[0]
dx = [count_male, count_female]
dx2 = pd.DataFrame(dx, index=["Male", "Female"])
st.bar_chart(dx2)