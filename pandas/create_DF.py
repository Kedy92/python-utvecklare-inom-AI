import pandas as pd
import numpy as np
import streamlit as st

# st.title("Jag vill kunna klara mig jättbra")
# st.header("This is my header")
# st.subheader("This is my subheader")

# st.text("Hello GeeksForGeeks!!!")

# st.markdown("### This is a markdown!!!!!!")

# st.success("success")
# st.info("Info here")
# st.warning("warning here")
# st.error("error here")
# exp = ZeroDivisionError("tried to divise by zero")
# st.exception(exp)

# st.write("Text with write")

# # Writing python inbuilt function range()

# st.write(range(10))

# from PIL import Image
#--------------------------------------
# img = Image.open("streamlit.png")

# st.image(img, width=200)
#----------------------------------------------
# from PIL import Image  # Import Image from Pillow
# img = Image.open("streamlit.png") # Open the image file
# st.image(img, width=200) # Display the image with a specified width
#-----------------------------------------
# if st.checkbox("Shows/Hide"):
#     st.text("Showing the widget")
#-----------------------------------------

# status = st.radio("Selct gender:", ["mal", "femal"])

# if status == "mal":
#     st.success("Mal")
# else:
#     st.success("Femal")

#---------------------------------------

# hobby = st.selectbox("Select a hobby", ['Dancing', 'Reading','Sport'])

# st.write("Your hobby is:", hobby)


# # Create a dropdown menu for selecting a hobby
# hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])

# # Display the selected hobby
# st.write("Your hobby is:", hobby)


# hobbies = st.multiselect("select hobbies", ["Dancing", "reading", "Sport"])

# st.write("Your selected:", len(hobbies), "hobbies")



# A simple button that does nothing
# st.button("Click Me")

# A button that displays text when clicked
# if st.button("About"):
#     st.text("Welcome to GeeksForGeeks!")

#---------------------------------------------

# name = st.text_input("Enter your name", "Type here...")

# if st.button("Submit"):
#     result = name.title()
#     st.success(result)

#---------------------------------------------

# level = st.slider("choose your level!", min_value=1, max_value=5)

# st.write(f"Slected level is: {level}")

#---------------------------------------------

# Tittle of the app

# st.title("BMI Calculator")

# # imput: weight in kilograms

# weight = st.number_input("Enter your weight (kg):", min_value=0.0, max_value="%.2f")

# # Input: height format selection

# height_unit = st.radio("Select you heigt unit: ", ['centimeters','Meters', 'feet'])

# # input height value based on selected unit

# height = st.number_input(f"Enter your height ({height_unit.lower()}):", min_value=0.0, format="%.2f")

# # Calculate BMI when button is pressed
# if st.button("Calculate BMI"):
#     try:
#         # Convert height to meters based on selected unit
#         if height_unit == 'Centimeters':
#             height_m = height / 100
#         elif height_unit == "Feet":
#             height = height / 3.28
#         else:
#             height_m = height
#         # Prevent division by zero

#         if height_m <= 0:
#             st.error("Height must be greater than zero")
#         else:
#             bmi = weight / (height_m ** 2)
#             st.success(f"Your BMI is {bmi:.2f}")

#             # BMI interpretation
#             if bmi < 16:
#                 st.error("You are Extremely Underweight")
#             elif 16 <= bmi < 18.5:
#                 st.warning("You are Underweight")
#             elif 18.5 <= bmi < 25:
#                 st.success("You are Healthy")
#             elif 25 <= bmi < 30:
#                 st.warning("You are Overweight")
#             else:
#                 st.error("You are Extremely Overweight")
#     except:
#         st.error("Please enter valid numeric values.")


#-------------------------------------------------------

import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Input: Weight in kilograms
weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")

# Input: Height format selection
height_unit = st.radio("Select your height unit:", ['Centimeters', 'Meters', 'Feet'])

# Input: Height value based on selected unit
height = st.number_input(f"Enter your height ({height_unit.lower()}):", min_value=0.0, format="%.2f")

# Calculate BMI when button is pressed
if st.button("Calculate BMI"):
    try:
        # Convert height to meters based on selected unit
        if height_unit == 'Centimeters':
            height_m = height / 100
        elif height_unit == 'Feet':
            height_m = height / 3.28
        else:
            height_m = height

        # Prevent division by zero
        if height_m <= 0:
            st.error("Height must be greater than zero.")
        else:
            bmi = weight / (height_m ** 2)
            st.success(f"Your BMI is {bmi:.2f}")

            # BMI interpretation
            if bmi < 16:
                st.error("You are Extremely Underweight")
            elif 16 <= bmi < 18.5:
                st.warning("You are Underweight")
            elif 18.5 <= bmi < 25:
                st.success("You are Healthy")
            elif 25 <= bmi < 30:
                st.warning("You are Overweight")
            else:
                st.error("You are Extremely Overweight")
    except:
        st.error("Please enter valid numeric values.")