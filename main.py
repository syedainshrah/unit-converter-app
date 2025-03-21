import streamlit as st

st.title("Conservation Calculator")
st.markdown("### Convert weight , lenght and time instantly ")

st.write("welcome! select a category , and enter a value to change instantly")

category = st.selectbox("choose a category ", ["weight", "length", "time"])

def convert_unit(category , value , unit ):
    if category == "length":
        if unit == "kilometer to miles":
            return value * 0.621371
        elif unit == "miles to kilometer":
            return value / 0.621371
        
    elif category == "weight":
        if unit == "kilogram to pound":
            return value * 2.20462
        elif unit == "pound to kilogram":
            return value / 2.20462
    
    elif category == "time":
        if unit == "hours to minutes":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "second to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "hours to day":
            return value * 24
        elif unit == "day to hours":
            return value / 24


if category == "length":
    unit = st.selectbox("select conversation" , ["kilometer to miles", "miles to kilometer"])
elif category ==  "weight":
    unit = st.selectbox("select conservation",["kilogram to pound", "pound to kilogram"])
elif category == "time":
    unit = st.selectbox("select conservation", ["hours to minutes", "minutes to hours",
                                              "seconds to minutes", "minutes to seconds",
                                              "hours to day", "day to hours"])

value = st.number_input("enter your value")

if st.button("convert"):
    result = convert_unit(category , value , unit )
    st.success(f"the result is {result:.2f}")

    

