from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np

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

st.subheader("ข้อมูลแยกตามเพศ")
count_male = dt.groupby('Sex').size()[1]
count_female = dt.groupby('Sex').size()[0]
dx = [count_male, count_female]
dx2 = pd.DataFrame(dx, index=["Male", "Female"])
st.bar_chart(dx2)

st.subheader("ข้อมูลค่าเฉลี่ยอายุแยกตามเพศ")
average_male_age = dt[dt['Sex'] == 1]['Age'].mean()
average_female_age = dt[dt['Sex'] == 0]['Age'].mean()
dxage = [average_male_age, average_female_age]
dxage2 = pd.DataFrame(dxage, index=["Male", "Female"])
st.bar_chart(dxage2)

html_8 = """
<div style="background-color:#6BD5DA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ทำนายข้อมูล</h5></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

A1 = st.number_input("กรุณาเลือกข้อมูลอายุ")
A2 = st.number_input("กรุณาเลือกข้อมูลเพศชาย=1 เพศหญิง=0")
A3 = st.number_input("กรุณาเลือกข้อมูลชนิดของการเจ็บหน้าอก")
A4 = st.number_input("กรุณาเลือกข้อมูล4")
A5 = st.number_input("กรุณาเลือกข้อมูล5")
A6 = st.number_input("กรุณาเลือกข้อมูล6")
A7 = st.number_input("กรุณาเลือกข้อมูล7")
A8 = st.number_input("กรุณาเลือกข้อมูล8")
A9 = st.number_input("กรุณาเลือกข้อมูล9")
A10 = st.number_input("กรุณาเลือกข้อมูล10")
A11 = st.number_input("กรุณาเลือกข้อมูล11")

if st.button("ทำนายผล"):
    #st.write("ทำนาย")
   dt = pd.read_csv("./data/Heart3.csv") 
   X = dt.drop('HeartDisease', axis=1)
   y = dt.HeartDisease 

   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)  
    
   x_input = np.array([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11]])
   st.write(Knn_model.predict(x_input))
   
   out=Knn_model.predict(x_input)

   if out[0] == 1:
    st.image("./img/HeartFailure.jpg")
   else:
    st.image("./img/heartOk.jfif")
else:
    st.write("ไม่ทำนาย")