import streamlit as st
import pandas as pd
import joblib


from src.custom_transformers import createDeck , createFamily , createTitle , ColumnDropper

# --- 1. Load the saved model pipeline ---
# Use st.cache_resource to prevent the model from being reloaded on every interaction
@st.cache_resource
def load_model():
    pipeline = joblib.load('models/model.pkl')
    return pipeline

model_pipeline = load_model()


# --- 2. Create the user interface for input ---
st.title("Titanic Survival Prediction 🚢")
st.sidebar.header("Passenger Details")

# Create input widgets in the sidebar
name = st.sidebar.text_input(
    'Name (in the format: Lastname, Title. Firstname)', 
    'Allen, Master. William Henry' # A good default to guide the user
)
pclass = st.sidebar.selectbox('Passenger Class (Pclass)', [1, 2, 3])
sex = st.sidebar.selectbox('Sex', ['male', 'female'])
age = st.sidebar.number_input('Age', min_value=0, max_value=100, value=30)
sibsp = st.sidebar.slider('Number of Siblings/Spouses Aboard (SibSp)', 0, 10, 1)
parch = st.sidebar.slider('Number of Parents/Children Aboard (Parch)', 0, 10, 0)
fare = st.sidebar.number_input('Fare', min_value=0.0, max_value=600.0, value=50.0)
embarked = st.sidebar.selectbox('Port of Embarkation (Embarked)', ['S', 'C', 'Q'])
# You will need widgets for all features your model was trained on: Ticket, Cabin, etc.
# For simplicity, we'll use placeholder values for some here.
ticket = "19947"
cabin = 'C52'


# --- 3. Process inputs and make prediction ---
if st.sidebar.button("Predict Survival"):

    # Create a DataFrame from the user inputs
    # The column names MUST match the names used during model training
    input_data = pd.DataFrame({
        'PassengerId' : 0,
        'Pclass': [pclass],
        'Name': [name],
        'Sex': [sex],
        'Age': [age],
        'SibSp': [sibsp],
        'Parch': [parch],
        'Ticket': [ticket],
        'Fare': [fare],
        'Cabin': [cabin],
        'Embarked': [embarked]
    })

    # Use the pipeline to predict
    prediction = model_pipeline.predict(input_data)[0]
    prediction_proba = model_pipeline.predict_proba(input_data)[0]

    # --- 4. Display the output ---
    st.header("Prediction Result")
    if prediction == 1:
        st.success("This passenger would likely have SURVIVED!")
        st.write(f"Confidence: {prediction_proba[1]*100:.2f}%")
    else:
        st.error("This passenger would likely have PERISHED.")
        st.write(f"Confidence: {prediction_proba[0]*100:.2f}%")