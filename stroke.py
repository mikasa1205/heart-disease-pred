# Import our packages
import streamlit as st
import joblib
import os
import numpy as np
from PIL import Image


attribute = ("""

## Attribute Information

1) id: unique identifier

2) gender: "Male", "Female" or "Other"

3) age: age of the patient

4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension

5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease

6) ever_married: "No" or "Yes"

7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"

8) Residence_type: "Rural" or "Urban"

9) avg_glucose_level: average glucose level in blood

10) bmi: body mass index

11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*

12) stroke: 1 if the patient had a stroke or 0 if not

""")


encoded_values = {"Female":0, "Male":1, "Yes":1, "No":0, "Urban":1, "Rural":0, 'Private':1,
 'Self-employed':3, 'Govt job':0, 'Children':4, 'Never worked':1, 'Formerly smoked':1, 'Never smoked':2, 'Smokes':3, 'Unknown':0}

# Function for encoding
def a(val, my_dict):
	for key, value in my_dict.items():
		if val == key:
			return value

def stroke_pred():

	st.write("# Stroke Predictor")
	img = Image.open("stroke.jpeg")
	st.image(img) 
	st.write("""

Stroke is a serious medical condition that can lead to long-term disability or death. Therefore, early prediction of stroke can help in effective prevention and management of the disease. With the advancements in machine learning and artificial intelligence, stroke prediction models can be developed that use various clinical and demographic factors to predict the risk of stroke.

Such models can be developed by collecting and analyzing data from large patient populations, which can help in identifying the factors that are strongly associated with stroke. These factors may include age, gender, smoking status, hypertension, body mass index, and previous history of stroke.

By using such stroke prediction models, healthcare providers can identify patients who are at a higher risk of stroke and provide them with appropriate preventive interventions, such as lifestyle modifications, medication, and regular monitoring. This can help in reducing the incidence of stroke and improving the quality of life of patients.
""")
	st.markdown(attribute)

	st.header("Give Your Input")
 

	col1, col2 = st.columns(2)

	with col1:
		gender = st.radio("What is your Gender", ["Male", "Female"])
		hypertension = st.radio("Do you have Hypertension?", ["Yes", "No"])
		ever_married = st.radio("Have you ever married before?", ["Yes", "No"])
		residence_type = st.selectbox("Select your Residence Type", ['Rural', 'Urban'])
		bmi = st.number_input("Enter your BMI Value", 10.0, 100.0, 28.0, step = 0.1)

	with col2:
		
		age = st.number_input("Enter your Age", 10, 90, 44)
		heart_disease = st.radio("Do you have Heart Disease?", ["Yes", "No"])
		work_type = st.selectbox("What is your Work type?", ['Private', 'Self-employed', 'Govt job', 'Children', 'Never worked'])
		avg_glucose_level = st.number_input("Enter your Avg glucose level", 55.0, 300.0, 106.0, step = 0.1)
		smoking_status = st.selectbox("Select your Smoking Status", ['Formerly smoked', 'Never smoked', 'Smokes', 'Unknown'])


	with st.expander("Your selected options"):
		so = {"Gender":gender,
		"Age":age, "hypertension":hypertension, "heart_disease":heart_disease, "ever_married":ever_married, 
		"work_type":work_type, "Residence_type":residence_type, 
		"avg_glucose_level":avg_glucose_level, "bmi":bmi,"smoking_status":smoking_status}

		st.write(so)


		result = []

		for i in so.values():
			if type(i) == int or type(i) == float:
				result.append(i)

			else:
				res = a(i, encoded_values)
				result.append(res)

		#st.write(result)

	with st.expander("Prediction Results"):

		input = np.array(result).reshape(1,-1)
		#st.write(input)

		m = joblib.load("stroke_model")

		prediction = m.predict(input)
		#st.write(prediction)

		prob = m.predict_proba(input)
		#st.write(prob)

		if prediction == 1:
			st.warning("Positive Risk!!! You have Stroke, Be Careful")
			prob_score = {"Positive Risk": prob[0][1],
			"Negative Risk": prob[0][0]}
			st.write(prob_score)

		else:
			st.success("Negative Risk!!! You don't have Stroke, Enjoy!!")
			prob_score = {"Negative Risk": prob[0][0],
			"Positive Risk": prob[0][1]}
			st.write(prob_score)