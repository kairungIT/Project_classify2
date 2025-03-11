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
