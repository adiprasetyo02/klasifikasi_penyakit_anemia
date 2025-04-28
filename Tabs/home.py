import streamlit as st

def app(data, x_resampled, y_resampled):

    # Title for the Home Page
    st.title('Aplikasi Klasifikasi Penyakit Anemia')

    # Description and instructions
    st.write("""
    Aplikasi ini digunakan untuk memprediksi apakah seseorang terkena anemia berdasarkan data hasil tes darah lengkap (CBC).
    Silakan pilih halaman **Prediction** untuk memulai prediksi.
    """)
