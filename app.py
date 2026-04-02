import streamlit as st
import numpy as np
import joblib
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="Heart Failure Prediction",
    page_icon="🫀",
    layout="centered" # Membuat tampilan terpusat
)

# Judul Utama dan Deskripsi (Sesuai Mockup)
st.title("Heart Failure Prediction")
st.markdown("""
The purpose of this machine learning is to predict the occurrence of heart failure (DEATH_EVENT) in patients using 12 medical features based on their medical history.
""")
st.divider()

# Fungsi untuk memuat model (di-cache untuk efisiensi)
@st.cache_resource
def load_model():
    model_path = "trained_model_rf.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.error(f"Error: Model file '{model_path}' tidak ditemukan. Pastikan file berada di folder yang sama.")
        return None

# Memuat model
model = load_model()

# Bagian Input Form (Menggunakan st.form agar input tidak run ulang setiap ketikan)
with st.form("heart_form"):
    st.markdown("---") # Garis pemisah visual

    # 1. Identify Patient
    st.subheader("Identify Patient")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age", placeholder="e.g. 50", help="Masukkan usia pasien")
    with col2:
        anaemia = st.text_input("Anemia (1=Yes, 0=No)", placeholder="e.g. 0")
    with col3:
        high_blood_pressure = st.text_input("High Blood Pressure (1=Yes, 0=No)", placeholder="e.g. 0")
    st.divider()

    # 2. Diagnosis
    st.subheader("Diagnosis")
    col4, col5 = st.columns(2)
    with col4:
        diabetes = st.text_input("Diabetes (1=Yes, 0=No)", placeholder="e.g. 0")
    with col5:
        ejection_fraction = st.text_input("Ejection Fraction", placeholder="e.g. 38")
    st.divider()

    # 3. Blood Features
    st.subheader("Blood Features")
    col6, col7, col8 = st.columns(3)
    with col6:
        creatinine_phosphokinase = st.text_input("Creatinine Phosphokinase", placeholder="e.g. 250")
    with col7:
        platelets = st.text_input("Platelets", placeholder="e.g. 263358.0")
    with col8:
        serum_sodium = st.text_input("Serum Sodium", placeholder="e.g. 137")
    st.divider()

    # 4. Patient Information
    st.subheader("Patient Information")
    col9, col10, col11, col12 = st.columns(4)
    with col9:
        serum_creatinine = st.text_input("Serum Creatinine", placeholder="e.g. 1.18")
    with col10:
        sex = st.text_input("Sex (1=Male, 0=Female)", placeholder="e.g. 1")
    with col11:
        smoking = st.text_input("Smoking (1=Yes, 0=No)", placeholder="e.g. 0")
    with col12:
        time = st.text_input("Time", placeholder="e.g. 130")
    
    st.markdown("---") # Garis pemisah visual
    
    # Tombol Prediksi (Sesuai Mockup)
    submitted = st.form_submit_button("Click Here to Predict", use_container_width=True)

# Logika Prediksi setelah tombol ditekan
if submitted and model:
    # Mengumpulkan input dan validasi
    try:
        # Konversi semua input menjadi float. Jika kosong atau bukan angka, akan error
        input_data = [
            float(age), float(anaemia), float(creatinine_phosphokinase),
            float(diabetes), float(ejection_fraction), float(high_blood_pressure),
            float(platelets), float(serum_creatinine), float(serum_sodium),
            float(sex), float(smoking), float(time)
        ]
        
        # Buat array numpy
        arr = np.array([input_data])
        
        # Prediksi
        pred = model.predict(arr)
        result = int(pred[0])
        
        # Tampilkan hasil
        st.divider()
        st.subheader("Prediction Result:")
        
        # Menampilkan hasil dengan status color (0=Success/Green, 1=Warning/Red)
        if result == 0:
            st.success(f"**Prediksi penyakit: {result}**")
            st.write("Pasien diprediksi berisiko **rendah** terhadap gagal jantung.")
        else:
            st.error(f"**Prediksi penyakit: {result}**")
            st.write("Pasien diprediksi berisiko **tinggi** terhadap gagal jantung.")
            
    except ValueError:
        st.error("Error: Pastikan semua input form terisi dengan angka valid.")
