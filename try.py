import streamlit as st


st.set_page_config(page_title="Ultimate Unit Converter 🌍", page_icon="🔄", layout="centered")


st.markdown(
    """
    <style>
        .big-title {
            font-size: 36px; 
            font-weight: bold; 
            text-align: center; 
            color: #ffffff;
            background: linear-gradient(to right, #0F2027, #203A43, #2C5364);
            padding: 10px; 
            border-radius: 10px;
        }
        .sub-title {
            font-size: 22px;
            text-align: center;
            color: #FFA500;
            margin-top: 10px;
        }
        .convert-box {
            background: #F8F9FA;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .footer {
            text-align: center;
            font-size: 18px;
            color: #ffffff;
            background-color: #000000;
            padding: 10px;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
    """, 
    unsafe_allow_html=True
)


st.markdown('<div class="big-title">🔄 Ultimate Unit Converter 🌍</div>', unsafe_allow_html=True)


unit_type = st.selectbox("Select a unit type to convert:", 
                         ["Length", "Weight", "Temperature", "Time", "Speed", "Area", "Volume"])


value = st.number_input("Enter the value to convert:", min_value=0.0, format="%.2f")


if unit_type == "Length":
    from_unit = st.selectbox("Convert from:", ["Meters", "Kilometers", "Miles", "Feet", "Inches"])
    to_unit = st.selectbox("Convert to:", ["Meters", "Kilometers", "Miles", "Feet", "Inches"])

    conversion_factors = {
        "Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084, "Inches": 39.3701
    }
    result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    unit_name = "length"

elif unit_type == "Weight":
    from_unit = st.selectbox("Convert from:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("Convert to:", ["Kilograms", "Grams", "Pounds", "Ounces"])

    conversion_factors = {
        "Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274
    }
    result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    unit_name = "weight"

elif unit_type == "Temperature":
    from_unit = st.selectbox("Convert from:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result = value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        result = (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result = value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        result = (value - 273.15) * 9/5 + 32
    else:
        result = value
    unit_name = "temperature"

elif unit_type == "Time":
    from_unit = st.selectbox("Convert from:", ["Seconds", "Minutes", "Hours", "Days"])
    to_unit = st.selectbox("Convert to:", ["Seconds", "Minutes", "Hours", "Days"])

    conversion_factors = {
        "Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400
    }
    result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    unit_name = "time"

elif unit_type == "Speed":
    from_unit = st.selectbox("Convert from:", ["m/s", "km/h", "mph"])
    to_unit = st.selectbox("Convert to:", ["m/s", "km/h", "mph"])

    conversion_factors = {
        "m/s": 1, "km/h": 3.6, "mph": 2.237
    }
    result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    unit_name = "speed"

elif unit_type == "Area":
    from_unit = st.selectbox("Convert from:", ["Square Meters", "Square Kilometers", "Acres", "Hectares"])
    to_unit = st.selectbox("Convert to:", ["Square Meters", "Square Kilometers", "Acres", "Hectares"])

    conversion_factors = {
        "Square Meters": 1, "Square Kilometers": 0.000001, "Acres": 0.000247105, "Hectares": 0.0001
    }
    result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    unit_name = "area"

elif unit_type == "Volume":
    from_unit = st.selectbox("Convert from:", ["Liters", "Milliliters", "Cubic Meters", "Gallons"])
    to_unit = st.selectbox("Convert to:", ["Liters", "Milliliters", "Cubic Meters", "Gallons"])

    conversion_factors = {
        "Liters": 1, "Milliliters": 1000, "Cubic Meters": 0.001, "Gallons": 0.264172
    }
    result = value * conversion_factors[to_unit] / conversion_factors[from_unit]
    unit_name = "volume"


if st.button("Convert Now 🔄"):
    st.markdown(f'<div class="convert-box">🎯 {value} {from_unit} equals <strong>{result:.4f} {to_unit}</strong> in {unit_name} conversion.</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="footer">🔥 Convert Everything, Anytime, Anywhere!<br>✨ Made by Zunaira Hussain ✨</div>',
    unsafe_allow_html=True
)
