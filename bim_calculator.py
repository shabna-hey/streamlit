import streamlit as st

st.header("BIM CALCULATOR")


num1=st.number_input("entre the weight",min_value=0.0)
num2=st.number_input("enter the height",min_value=0.0)

btn = st.button("Calculate BMI")

if btn:
    bmi = num1 / ((num2/100)**2)
    st.write("BMI =", bmi)
    if bmi < 18.5:
        st.info("Underweight")
    elif bmi < 25:
        st.success("Normal weight")
    elif bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Obesity")