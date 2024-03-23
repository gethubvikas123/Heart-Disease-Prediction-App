import numpy as np
import joblib
import pandas as pd
import streamlit as st 



model = joblib.load(r'heart_disease_prediction_model.joblib', mmap_mode=None)


def predict_heart_disease(input_data):
  input_data_as_numpy_array= np.asarray(input_data)
  input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

  prediction = model.predict(input_data_reshaped)
  print(prediction)

  if (prediction[0]== 0):
    return('The Person does not have a Heart Disease')
  else:
    return('The Person has Heart Disease')
col1, col2 = st.columns([2, 3])

# Displaying dashboard title
with col2:
    heart_logo_url = r"Image_A1-9-576x486.jpg"
    st.image(heart_logo_url, width=350) 

# Displaying logo
with col1:
    st.title('Heart Disease Prediction App')


age = st.sidebar.number_input('Enter your age: ')
sex  = st.sidebar.selectbox('Sex',(0,1))
cp = st.sidebar.selectbox('Chest pain type',(0,1,2,3))
trestbps = st.sidebar.number_input('Resting blood pressure: ')
chol = st.sidebar.number_input('Serum cholestoral in mg/dl: ')
fbs = st.sidebar.selectbox('Fasting blood sugar',(0,1))
restecg = st.sidebar.selectbox('Resting electrocardiographic results: ',(0,1,2))
thalach = st.sidebar.number_input('Maximum heart rate achieved: ')
exang = st.sidebar.selectbox('Exercise induced angina: ',(0,1))
oldpeak = st.sidebar.number_input('oldpeak ')
slope = st.sidebar.selectbox('slope of the peak exercise ST segmen: ',(0,1,2))
ca = st.sidebar.selectbox('number of major vessels',(0,1,2,3,4))
thal = st.sidebar.selectbox('thal',(0,1,2,3))

prediction_value = ''

if st.button("Check Disease"):
        
     prediction_value= predict_heart_disease([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])

st.success(prediction_value)

st.title("Description")

col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1, 1])

with col1:
   st.write("Sex")
   st.write("0 : Female")
   st.write("1 : Male")

with col2:
   st.write("Chest pain type")
   st.write("0: Typical Angina")
   st.write("1: Atypical Angina ")
   st.write("2: Non-anginal Pain")
   st.write("3: Asymptomatic")


with col3:
   st.write("Fasting blood sugar")
   st.write("0: Fasting blood sugar level < 120 mg/dL (Normal)  ")
   st.write("1: Fasting blood sugar level ≥ 120 mg/dL (Abnormal)")


with col4:
   st.write("Resting electrocardiographic")
   st.write("0: Normal ")
   st.write("1: depression ")
   st.write("2: Showing probable")

with col5:
   st.write("Exercise induced angina")
   st.write("0: Absence of exercise-induced angina (No) ")
   st.write("1: Presence of exercise-induced angina (Yes)")


with col6:
   st.write("slope of the peak exercise ST segmen")
   st.write("0: Upsloping")
   st.write("1: Flat ")
   st.write("2: Downsloping")


with col7:
   st.write("thal")
   st.write("0: Normal ")
   st.write("1: Fixed Defect ")
   st.write("2: Reversible Defect")
   st.write("3: Unknown")


