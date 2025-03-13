import streamlit as st
import pandas as ps
st.title("BMI CALCULATOR")
height=st.slider("Enter your Height (in cm): ",100,250,170)
weight=st.slider("Enter your Weight (in KG): ",40,200,70)
bmi=weight/((height/100)**2)
st.write(f"Your BMI is {bmi:.2f}")
st.write("### BMI Categories")
st.write("Underweight__BMI less then 18.5")
st.write("-Normal Weight : BMI Between 18.5 and 24.9")
st.write("Overweight: BMI between 25 and 29.9")
st.write("Obesity: BMI 30 or Greater")
