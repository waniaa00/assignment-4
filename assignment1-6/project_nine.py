import streamlit as st

st.title("✨ My First Streamlit Website")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])

if page == "Home":
    st.header("Welcome to My Streamlit Website! 🎊")
    st.write("This is a simple web app built with Streamlit.")


    name = st.text_input("Enter your name:")
    if st.button("Submit"):
        st.success(f"Hello, {name}! 👋")



elif page == "About":
    st.header("About This App🔎")
    st.write("This is a Streamlit app built in under 15 minutes.")


st.write("----------")
st.write("🔹  Developed by [Wania Akram](https://github.com/waniaa00)  &nbsp;|&nbsp;  Innovate Faster! 🔹")
