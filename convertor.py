import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-image: url('https://www.w3schools.com/w3images/mountains.jpg'); /* Example background image URL */
        background-size: cover;
        color: white;
    }
    .stApp {
        background: rgba(30, 30, 47, 0.8); /* Semi-transparent background for better readability */
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: #FFD700; /* Gold color for the title */
    }
    .stButton > button {
        background: linear-gradient(45deg, #FF6347, #FF4500); /* Tomato to OrangeRed gradient */
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(255, 69, 0, 0.4); /* OrangeRed shadow */
    }
    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff); /* LightGreen to SkyBlue gradient */
        color: black;
    }
    .result-box {
        color: white;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 225, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #FFD700; /* Gold color for the footer text */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.markdown("<h1>Unit Convertor Using Python and Streamlit 🌐</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature. 🔧📏")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Select Conversion Type 📊", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert 🎯", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1000000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value
    
# Conversion button
convert_button = st.button("✔ Convert")
if convert_button:
    if conversion_type == "Length":
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_conversion(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_conversion(value, from_unit, to_unit)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit} 🎉</div>", unsafe_allow_html=True)
    st.session_state["converted"] = True

if "converted" in st.session_state and st.session_state["converted"]:
    st.write("<p style='color: white;'>Conversion complete!</p>", unsafe_allow_html=True)
    st.session_state["converted"] = False

st.markdown("<div class='footer'>Developed by Zeeshan Haider using Python and Streamlit 🚀</div>", unsafe_allow_html=True)
