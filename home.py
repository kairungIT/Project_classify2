import streamlit as st
import pandas as pd

st.title("👩‍⚕️👩‍⚕️การพยากรณ์โรคหัวใจล้มเหลวด้วยเทคนิคเหมืองข้อมูล👩‍⚕️👩‍⚕️")
st.header("👩‍⚕️👩‍⚕️การพยากรณ์โรคหัวใจล้มเหลวด้วยเทคนิคเหมืองข้อมูล👩‍⚕️👩‍⚕️")

st.image('./img/heart1.jfif')
st.subheader("โรคหัวใจล้มเหลว")

dt=pd.read_csv('./data/Heart3.csv')
st.header("ข้อมูลโรคหัวใจ")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลโรคหัวใจ")
st.write('ผลรวม')
