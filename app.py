# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('heartdisease_model.sav', 'rb'))


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
    
    age=st.text_input('Age in years')
    sex=st.text_input('Sex(1:male; 0:female)')
    cp=st.text_input('Chest pain type')
    trestbps=st.text_input('Resting blood pressure(in mm Hg)')
    chol=st.text_input('Serum Cholestoral(in mg/dl)')
    fbs=st.text_input('Fasting blood sugar>120 mg/dl(1:true, 0:false)')
    restecg=st.text_input('Resting Ecg')
    thalach=st.text_input('Maximum heart rate achieved')
    exang=st.text_input('Exercise induced angina(1:yes, 0:no)')
    oldpeak=st.text_input('Oldpeak')
    slope=st.text_input('Slope')
    ca=st.text_input('Number of major vessels')
    thal=st.text_input('Thal')
    
    #code for prediction
    diagnosis=''
    
    #creating a button for prediction
    if st.button('Get the Result'):
        diagnosis= heartdiseaseprediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    
    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()
