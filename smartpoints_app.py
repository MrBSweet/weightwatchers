import streamlit as st

def calculate_smartpoints(calories, saturated_fat, sugar, protein):
    smartpoints = (calories * 0.0305) + (saturated_fat * 1.275) + (sugar * 0.12) - (protein * 0.098)
    return round(smartpoints)

st.title("Weight Watchers SmartPoints Calculator")

calories = st.number_input("Enter the number of calories:", min_value=0.0)
saturated_fat = st.number_input("Enter the amount of saturated fat (in grams):", min_value=0.0)
sugar = st.number_input("Enter the amount of sugar (in grams):", min_value=0.0)
protein = st.number_input("Enter the amount of protein (in grams):", min_value=0.0)

if st.button("Calculate SmartPoints"):
    smartpoints = calculate_smartpoints(calories, saturated_fat, sugar, protein)
    st.write(f"The Weight Watchers SmartPoints value is: {smartpoints}")
