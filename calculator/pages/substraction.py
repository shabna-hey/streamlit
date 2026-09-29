import streamlit as st

num1=st.number_input("enter the number 1",min_value=0)
num2=st.number_input("enter the number 2",min_value=0)
btn=st.button("substraction")
if btn:
    s=(num1-num2)
    st.write("sum=" ,s)
