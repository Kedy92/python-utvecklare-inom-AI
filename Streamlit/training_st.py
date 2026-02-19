import streamlit as st

# # Calculate BMI(body mass index)

# st.title("BMI Calculator")

# weight = st.number_input("Enter your waight:", min_value=0.0, format="%.2f")

# height_unit = st.radio("Select your weight unit:", ["Centimeters", "Metters", "Feet"])

# height = st.number_input(f"Enter your height here ({height_unit })", min_value=0.0, format="%.2f")


# if st.button("Calculate BMI"):
#     try:
#         if height_unit == "Centimenters":
#             height_m = height / 100
#         elif height_unit =="'feet":
#             height_m = height / 3.28
#         else:
#             height_m = height

#         if height_m <=0:
#             st.error("Height must be greater than zero.")
#         else:
#             bmi= weight / (height_m **2)
#             st.success("Your BMI is", bmi)
        
#         # BMI interpretation

#         if bmi <= 16:
#             st.error("You are Extremely Underweight")
#         elif 16 <= bmi < 18.5:
#             st.warning("You are Underweight")
#         elif 18.5 <= bmi < 25:
#             st.success("You are Healthy")
#         elif 25 <= bmi < 30:
#             st.warning("You are Overweight")
#         else:
#             st.error("You are Extremely Overweight")
    
#     except:
#         st.error("Please enter valid numeric values.")

#------------------------------------------------------------


st.set_page_config(layout="wide")
st.title("Streamlit Part 4: Inputs in Streamlit")

col1, col2 = st.columns(2)


with col1:
    st.subheader("1. Button")
    btn1 = st.button("Click Me", key="button", help="Click me to see the magic", type='secondary', disabled=False)
    if btn1:
        st.write("Button Clicked")
    
    st.subheader("2. Link Button")
if st.link_button("Click Me", "<https://www.streamlit.io/>"):
    st.write("Link Button Clicked")

st.subheader("3. Download Button")
if st.download_button("Download Me", "hello world", "hello.txt", mime='text/plain'):
    st.write("Download Button Clicked")


st.subheader("4. Checkbox")
checkbox_val = st.checkbox("Check Me", value=False)
if checkbox_val:
    st.write("Checkbox Checked")

st.subheader("5. Radio")
radio_val = st.radio("Select Color", ["Red", "Green", "Blue"], index=0)
if radio_val:
    st.write(f"You selected {radio_val}")

st.subheader("6. Selectbox")
select_val = st.selectbox("Select Color", ["Red", "Green", "Blue", "Black"], index=1)
if select_val:
    st.write(f"You selected {select_val}")

st.subheader("7. Multiselect")
multiselect_val = st.multiselect("Select Colors", ["Red", "Green", "Blue", "Black"], default=["Red"])
if multiselect_val:
    st.write(f"You selected {multiselect_val}")

st.subheader("8. Select Slider")
select_slider_val = st.select_slider("Select Value", options=range(1, 101), value=50)
if select_slider_val:
    st.write(f"You selected {select_slider_val}")

with col2:
    st.subheader("9. Text Input")
    text_input_val = st.text_input("Enter some text", value="", max_chars=50)
    if text_input_val:
        st.write(f"You entered {text_input_val}")

st.subheader("10. Text Area")
text_area_val = st.text_area("Enter some text", value="", height=150, max_chars=200)
if text_area_val:
    st.write(f"You entered {text_area_val}")

st.subheader("11. Number Input")
number_input_val = st.number_input("Enter a number", value=0, min_value=0, max_value=100, step=1)
if number_input_val:
    st.write(f"You entered {number_input_val}")

st.subheader("12. Date Input")
date_input_val = st.date_input("Enter a date")
if date_input_val:
    st.write(f"You selected {date_input_val}")

st.subheader("13. Time Input")
time_input_val = st.time_input("Enter a time")
if time_input_val:
    st.write(f"You selected {time_input_val}")

st.subheader("14. File Uploader")
file_uploader_val = st.file_uploader("Upload a file", type=["png", "jpg", "txt"])
if file_uploader_val:
    st.write(f"You uploaded {file_uploader_val.name}")


st.subheader("15. Color Picker")
color_picker_val = st.color_picker("Pick a color", value="#00f900")
if color_picker_val:
    st.write(f"You picked {color_picker_val}")


st.subheader("16. Camera Input")
camera_input_val = st.camera_input("Take a picture", help="Capture an image using your camera")
if camera_input_val:
    st.write("Picture captured successfully")