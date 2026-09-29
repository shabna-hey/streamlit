import streamlit as st


#number_input()
num1=st.number_input("enter the number1",min_value=0)
num2=st.number_input("enter the number2",min_value=0)
st.write(num1)
st.write(num2)

#text_input()
name=st.text_input("enter the name")
st.write(name)

#date
date=st.date_input("enter date")
st.write(date)

#button
btn=st.button("click")
print(btn)
if btn:
    st.write(num1)
    st.write(num2)
    st.write(name)
    st.write(date)
#radio
g=st.radio("gender",['male','female'])
st.write(g)
#checkbox
a=st.checkbox("python")
st.write(a)

#select
l=st.selectbox("places",['mapm','ernk'])
st.write(l)