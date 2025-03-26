import streamlit as st

# streamlit run app.py

st.title("Streamlit Demo")

st.header("Header of demo page")

st.subheader("sub-header of streamlit")

st.write("hello mintra")

st.success("success tag")

st.warning("warning tag")

st.info("info tag")

st.error("error tag")

if st.checkbox("Select/Unselect"):
    st.text("User selected the checkbox")
else:
    st.text("User has not selected the checkbox")

state = st.radio("What is your favourite colour?", ("red", "green", "yellow"))

if state == 'green':
    st.success("That's my favourite colour as well")
else:
    st.info("That's not my favourite colour")

occupation = st.selectbox("What do you do?", ["Student", "Vlogger", "Engineer"])

st.text(f"selected option is {occupation}")
st.text(f"selected colour is {state}")

if st.button("Example Button"):
    st.error("You clicked it")

st.sidebar.header("sidebar header")

st.sidebar.text("sidebar body")
