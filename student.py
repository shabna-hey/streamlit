import streamlit as st
from datetime import date
st.subheader("STUDENT REGISTRATION FORM")
name=st.text_input("name")
age=st.number_input("age",min_value=0)
DOB=st.date_input("DOB",min_value=date(1990,1,1),
                  max_value=date.today(),
                  value=date(2026,1,1))

email=st.text_input("email")
g=st.radio("gender",['male','female'])
a=st.selectbox("courses",['python','java','data','anylist'])


btn=st.button("click")
print(btn)
if btn:
    st.write("name:",name)
    st.write("age:",age)
    st.write("DOB:",DOB)
    st.write("email:",email)
    st.write("gender:",g)
    st.write("courses:",a)