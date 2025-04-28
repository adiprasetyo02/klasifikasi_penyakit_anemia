import streamlit as st
from web_functions import load_data  # Function to load dataset and preprocess data
from Tabs import home, prediction  # Import home and prediction pages

Tabs = {
    "Home": home,
    "Prediction": prediction
}

# Sidebar navigation
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", list(Tabs.keys()))

# Load dataset (only once)
data, x_resampled, y_resampled = load_data()

def app(data, x_resampled, y_resampled):
    if page == "Prediction":
        Tabs[page](data, x_resampled, y_resampled)
    else:
        Tabs[page]()  # Untuk halaman Home


# Run the app
app(data, x_resampled, y_resampled)
