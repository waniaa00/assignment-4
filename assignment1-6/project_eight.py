import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def main():
    st.title("🧮 Simple BMI Calculator")
    
    st.write("Enter your height and weight to calculate your BMI:")

    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
    height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.75)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.success(f"Your BMI is: {bmi:.2f}")

        # Health message
        if bmi < 18.5:
            st.warning("🟡 You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.info("🟢 You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("🟠You are overweight.")
        else:
            st.error("🔴 You are obese.")

if __name__ == "__main__":
    main()


st.write("----------")
st.write("🔹  Developed by [Wania Akram](https://github.com/waniaa00)  &nbsp;|&nbsp;  Fast, Safe, and Secure! 🔹")