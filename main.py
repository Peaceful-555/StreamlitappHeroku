# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/JAY/OneDrive/Desktop/ML model as an api/MLmodel/heartdisease_model.sav', 'rb'))


def heartdiseaseprediction(input_data):

    # change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
       return 'The Person does not have a Heart Disease'
    else:
       return 'The Person has Heart Disease'

def main():
    
    #giving a title
    st.title('Heart Disease prediction Web App')
    
    #getting input data from user
    
    age=st.text_input('age')
    sex=st.text_input('sex')
    cp=st.text_input('chest_pain')
    trestbps=st.text_input('restbp')
    chol=st.text_input('cholestoral')
    fbs=st.text_input('fasting_blood_sugar')
    restecg=st.text_input('restecg')
    thalach=st.text_input('max_heart_rate')
    exang=st.text_input('exercise_angina')
    oldpeak=st.text_input('oldpeak')
    slope=st.text_input('slope')
    ca=st.text_input('major_vessels')
    thal=st.text_input('thal')
    
    #code for prediction
    diagnosis=''
    
    #creating a button for prediction
    if st.button('Get the Result'):
        diagnosis= heartdiseaseprediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    
    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()
