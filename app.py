# importing the packages
import streamlit as st
from PIL import Image


# importingthe files
from heart import heart_pred
from cancer import cancer_pred
from diabetes import diabetes_pred
from stroke import stroke_pred
from kidney import kidney_pred

def main():

	menu = ["Home", "Diabetes Prediction", "Heart Disease Prediction", "Chronic Kidney Disease Prediction", "Stroke Prediction",
	"Cancer Prediction", "About"]

	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Home":

		st.write("# Multiple Disease Predictor App")
		#img = Image.open("cover.jpg")
		#st.image(img)

		st.write("""


A multiple disease prediction system is an advanced healthcare technology that uses machine learning algorithms to predict the likelihood of a patient developing multiple diseases based on their medical history, lifestyle, genetic factors, and other relevant data. The system is designed to help doctors and medical professionals identify patients who are at a higher risk of developing multiple diseases and provide them with early intervention and appropriate medical care to prevent or manage the onset of these diseases. This system can have a significant impact on the healthcare industry by improving patient outcomes, reducing healthcare costs, and enhancing overall population health.


There are a total of 5 diseases that can be predicted with the help of this application.

### App Content

	- This app has 7 sections

	1) Home Page - The page you are currently in

	2) Diabetes Prediction - This page will help you to predict whether you have 
	Diabetes or not

	3) Heart Disease Prediction - This page will help you to predict whether you have 
	Heart disease or not

	4) Chronic Kidney Disease Prediction - This page will help you to predict whether 
	you have Chronic Kidney Disease or not

	5) Liver Disease Prediction - This page will help you to predict whether you have 
	Liver Disease or not

	6) Cancer Prediction - This page will help you to predict whether you have Cancer 
	or not

	7) About - About the Creators

			""")


	elif choice=="Heart Disease Prediction":
		heart_pred()
	elif choice == "Cancer Prediction":
		cancer_pred()
	elif choice == "Diabetes Prediction":
		diabetes_pred()
	elif choice == "Stroke Prediction":
		stroke_pred()
	elif choice == "Chronic Kidney Disease Prediction":
		kidney_pred()
	else:

		st.subheader("About the Creators")
		col1, col2 = st.columns(2)
		with col1:
			
			st.write("### Adith Sreeram")
			img = Image.open("asr.jpeg")
			st.image(img)

			st.text("""

			I am a currently pursuing my Bachelors in 
			Computer Science with a Specialization in 
			Data Analytics. 
			I am passionate about using data-driven 
			approaches to solve complex problems and 
			improve decision-making. 
			During my studies, I worked on various 
			projects that involved analyzing and 
			visualizing large datasets, 
			building predictive models, and 
			implementing machine learning algorithms. 
			These experiences sparked my interest in 
			pursuing a career in data science and I 
			am excited to continue learning and 
			growing in this field. 
			I'm a quick learner and a team player, 
			and I can't wait to contribute to 
			meaningful projects.
			
					""")

			socials = ["LinkedIn", "Github", "GMail"]
			linkedin = "http://www.linkedin.com/in/asr373"
			github = "https://github.com/ASR373"
			mail = "adithnadar@gmail.com"
			with st.expander("Link to my Socials"):
				a = st.selectbox("Social", socials)
				if a =="LinkedIn":
					st.write(linkedin)
				elif a =="Github":
					st.write(github)
				elif a=="GMail":
					st.write(mail)

		with col2:
			
			st.write("### Jithendra Sai")
			img = Image.open("sai.jpeg")
			st.image(img)

			st.text("""

			I am a currently pursuing my Bachelors in 
			Computer Science with a Specialization in 
			Data Analytics.
			I have experience working with big data 
			and building predictive models, and I'm 
			excited to learn more about data 
			visualization and communicating insights 
			effectively. 
			I'm a creative problem-solver and a curious 
			learner, and I'm eager to contribute to 
			innovative projects.
			I'm excited to apply my skills to real-world 
			problems and collaborate with experienced 
			professionals in the field.
			
					""")

			socials = ["LinkedIn", "Github", "GMail"]
			linkedin = "https://www.linkedin.com/in/jithendra-sai-8b2b541b8/"
			github = "https://github.com/jithendrasai1"
			mail = "jithendrasaipappuri@gmail.com"
			with st.expander("Links to my Socials"):
				a = st.selectbox("Socials", socials)
				if a =="LinkedIn":
					st.write(linkedin)
				elif a =="Github":
					st.write(github)
				elif a=="GMail":
					st.write(mail)


main()