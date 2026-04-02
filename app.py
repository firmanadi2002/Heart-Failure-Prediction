import streamlit as st
import numpy as np
import joblib

# Konfigurasi halaman UI
st.set_page_config(
    page_title="Heart Failure Prediction", 
    page_icon="🫀", 
    layout="centered"
)

# Load model (Menggunakan st.cache_resource agar model tidak di-load ulang setiap interaksi user)
@st.cache_resource
def load_model():
    # Pastikan file model berada di satu folder yang sama
    return joblib.load("trained_model_rf.pkl")

model = load_model()

# Header halaman
st.title("🫀 Heart Failure Prediction")
st.markdown("Aplikasi web ini memprediksi risiko gagal jantung berdasarkan parameter rekam medis pasien. Silakan masukkan data pada form di bawah ini.")
st.divider()

# Membuat form input
with st.form("prediction_form"):
    st.subheader("Data Pasien")

    # Menggunakan layout kolom agar form tidak terlalu panjang ke bawah
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=50)
        anaemia = st.selectbox("Anaemia", options=["No", "Yes"])
        creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase", min_value=0, value=250)
        diabetes = st.selectbox("Diabetes", options=["No", "Yes"])
        ejection_fraction = st.number_input("Ejection Fraction (%)", min_value=0, max_value=100, value=38)
        high_blood_pressure = st.selectbox("High Blood Pressure", options=["No", "Yes"])

    with col2:
        platelets = st.number_input("Platelets", min_value=0.0, value=263358.0)
        serum_creatinine = st.number_input("Serum Creatinine", min_value=0.0, value=1.18, step=0.1)
        serum_sodium = st.number_input("Serum Sodium", min_value=0, value=137)
        sex = st.selectbox("Sex", options=["Female", "Male"])
        smoking = st.selectbox("Smoking", options=["No", "Yes"])
        time = st.number_input("Time (Follow-up period in days)", min_value=0, value=130)

    # Tombol submit khusus form
    submit_button = st.form_submit_button("Predict", type="primary", use_container_width=True)

# Logika ketika tombol dipencet
if submit_button:
    # Mengonversi input selectbox kembali menjadi angka (1.0 atau 0.0) sesuai permintaan model ML
    anaemia_val = 1.0 if anaemia == "Yes" else 0.0
    diabetes_val = 1.0 if diabetes == "Yes" else 0.0
    hbp_val = 1.0 if high_blood_pressure == "Yes" else 0.0
    sex_val = 1.0 if sex == "Male" else 0.0
    smoking_val = 1.0 if smoking == "Yes" else 0.0

    # Menyusun data ke dalam Numpy array
    input_data = np.array([[
        float(age), anaemia_val, float(creatinine_phosphokinase),
        diabetes_val, float(ejection_fraction), hbp_val,
        float(platelets), float(serum_creatinine), float(serum_sodium),
        sex_val, smoking_val, float(time)
    ]])

    # Melakukan prediksi
    prediction = model.predict(input_data)
    result = int(prediction[0])

    # Menampilkan hasil dengan alert yang sesuai
    st.divider()
    st.subheader("Hasil Prediksi")
    if result == 1:
        st.error("⚠️ Prediksi Penyakit: **1** (Pasien diprediksi berisiko tinggi terhadap gagal jantung)")
    else:
        st.success("✅ Prediksi Penyakit: **0** (Pasien diprediksi berisiko rendah)")
