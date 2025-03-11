import streamlit as st
import pandas as pd

st.header("👩‍⚕️👩‍⚕️การพยากรณ์โรคหัวใจล้มเหลวด้วยเทคนิคเหมืองข้อมูล👩‍⚕️👩‍⚕️")
c1,c2,c3=st.column(3)
with c1:
with c2:
        st.image('./img/heart1.jfif')
with c3:

dt= pd.read_csv('./data/Heart3.csv')

st.header("ข้อมูลโรคหัวใจ")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลโรคหัวใจ")
st.write('ผลรวม')
