import streamlit as st
from web_functions import train_model, predict

def apps(data, x_resampled, y_resampled):
    st.title("Halaman Prediksi Penyakit Anemia")

    # input untuk setiap fitur CBC menggunakan number_input
    col1, col2 = st.columns(2)

    with col1:
        WBC = st.number_input('Masukkan nilai WBC (contoh: 5.0)', min_value=0.0, format="%.2f")
    with col2:
        LYMp = st.number_input('Masukkan nilai LYMp (contoh: 35.0)', min_value=0.0, format="%.2f")
    with col1:
        NEUTp = st.number_input('Masukkan nilai NEUTp (contoh: 55.0)', min_value=0.0, format="%.2f")
    with col2:
        LYMn = st.number_input('Masukkan nilai LYMn (contoh: 2.1)', min_value=0.0, format="%.2f")
    with col1:
        NEUTn = st.number_input('Masukkan nilai NEUTn (contoh: 3.3)', min_value=0.0, format="%.2f")
    with col2:
        RBC = st.number_input('Masukkan nilai RBC (contoh: 4.7)', min_value=0.0, format="%.2f")
    with col1:
        HGB = st.number_input('Masukkan nilai HGB (contoh: 14.0)', min_value=0.0, format="%.2f")
    with col2:
        HCT = st.number_input('Masukkan nilai HCT (contoh: 42.0)', min_value=0.0, format="%.2f")
    with col1:
        MCV = st.number_input('Masukkan nilai MCV (contoh: 89.0)', min_value=0.0, format="%.2f")
    with col2:
        MCH = st.number_input('Masukkan nilai MCH (contoh: 30.0)', min_value=0.0, format="%.2f")
    with col1:
        MCHC = st.number_input('Masukkan nilai MCHC (contoh: 33.5)', min_value=0.0, format="%.2f")
    with col2:
        PLT = st.number_input('Masukkan nilai PLT (contoh: 250)', min_value=0.0, format="%.2f")
    with col1:
        PDW = st.number_input('Masukkan nilai PDW (contoh: 12.0)', min_value=0.0, format="%.2f")
    with col2:
        PCT = st.number_input('Masukkan nilai PCT (contoh: 0.2)', min_value=0.0, format="%.2f")

    # Prediction button
    if st.button("Prediksi"):
        # Kumpulkan semua masukan ke dalam sebuah daftar
        features = [WBC, LYMp, NEUTp, LYMn, NEUTn, RBC, HGB, HCT, MCV, MCH, MCHC, PLT, PDW, PCT]

        # Periksa apakah ada nilai input yang tidak valid (0 atau kosong, atau ada nilai yang hilang)
        if any(val == 0.0 for val in features):
            st.error("Harap isi semua nilai fitur dengan benar (nilai tidak boleh 0.0).")
            return

        try:
            # Latih model menggunakan data yang diambil sampelnya
            dt_model, model_score = train_model(x_resampled, y_resampled)

            # Buat prediksi dan dapatkan probabilitas prediksi
            result = predict(dt_model, features)
            predicted_label, prediction_proba = result

            # List of possible diagnoses (labels) that match the order of your classes
            diagnosis_labels = [
                'Normocytic hypochromic anemia',
                'Iron deficiency anemia',
                'Other microcytic anemia',
                'Leukemia',
                'Healthy',
                'Thrombocytopenia',
                'Normocytic normochromic anemia',
                'Leukemia with thrombocytopenia',
                'Macrocytic anemia'
            ]

            # Map the prediction index to the actual diagnosis label
            if predicted_label in diagnosis_labels:
                predicted_index = diagnosis_labels.index(predicted_label)
                probability = prediction_proba[predicted_index] * 100  # Get the percentage probability

                # Display the prediction results
                st.info("Prediksi sukses...")
                st.write(f"Jenis Anemia: {predicted_label}")
                st.write(f"Tingkat Keyakinan: {probability:.2f}%")

                # Show a message based on the predicted label
                if "anemia" in predicted_label.lower():
                    st.warning("Orang tersebut rentan terkena penyakit anemia.")
                else:
                    st.success("Orang tersebut relatif aman dari penyakit anemia.")

                # Display the accuracy of the model
                st.write(f"Model yang digunakan memiliki tingkat akurasi {model_score * 100:.2f}%")
            else:
                st.error("Label prediksi tidak valid.")

        except ValueError as e:
            st.error(f"Terjadi kesalahan dalam proses prediksi: {e}")
        except Exception as e:
            st.error(f"Terjadi kesalahan yang tidak terduga: {e}")

