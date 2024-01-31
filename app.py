import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('my_model.pkl', 'rb'))


# creating a function for Prediction

def heart_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The Person does not have a Heart Disease'
    else:
        return 'The person has Heart Disease'


def main():
    # giving a title
    st.title('Heart Prediction Web App')

    # getting the input data from the user

    age = st.text_input('age')
    sex = st.text_input('sex')
    cp = st.text_input('chest pain type')
    trestbps = st.text_input('resting blood pressure')
    chol = st.text_input('serum cholestoral')
    fbs = st.text_input('fasting blood sugar')
    restecg = st.text_input('Diabetes Pedigree Function value')
    thalach = st.text_input('maximum heart rate achieved')
    exang = st.text_input('exercise induced angina')
    oldpeak = st.text_input('oldpeak')
    slope = st.text_input('the_slope_of_the_peak_exercise_ST_segment')
    ca = st.text_input('number_of_major_vessels_colored_by_flourosopy')
    thal = st.text_input("thal")

    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Test Result'):
        diagnosis = heart_prediction(
            [int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach) ,int(exang),float(oldpeak),
             int(slope),int(ca),int(thal)])

    st.success(diagnosis)


if __name__ == '__main__':
    main()
