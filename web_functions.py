import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
import streamlit as st

# Load the dataset
@st.cache_data
def load_data():
    # Load CSV data
    url = 'https://raw.githubusercontent.com/adiprasetyo02/klasifikasi_penyakit_anemia/refs/heads/main/diagnosed_cbc_data_v4.csv'
    data = pd.read_csv(url)
    x = data[['WBC', 'LYMp', 'NEUTp', 'LYMn', 'NEUTn', 'RBC', 'HGB', 'HCT', 
              'MCV', 'MCH', 'MCHC', 'PLT', 'PDW', 'PCT']]  # Features
    y = data['Diagnosis']  # Target column (Diagnosis)

    return data, x, y

# Split data into training and testing sets
@st.cache_data
def split_data(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    return x_train, x_test, y_train, y_test

# Apply SMOTE to balance the dataset
@st.cache_data
def apply_smote(x_train, y_train):
    smote = SMOTE(random_state=42)
    x_resampled, y_resampled = smote.fit_resample(x_train, y_train)
    return x_resampled, y_resampled

# Train the model
@st.cache_resource
def train_model(x_resampled, y_resampled):
    dt_model = DecisionTreeClassifier(random_state=50)
    dt_model.fit(x_resampled, y_resampled)
    score = dt_model.score(x_resampled, y_resampled)
    return dt_model, score

# Make predictions
def predict(dt_model, features):
    # Get the prediction
    prediction = dt_model.predict([features])[0]
    
    # Get the prediction probabilities for each class
    prediction_proba = dt_model.predict_proba([features])[0]
    
    return prediction, prediction_proba

