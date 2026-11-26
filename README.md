# 🫀 Heart Failure Prediction — End-to-End Machine Learning App

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Random%20Forest-F7931E?logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)

Sistem klasifikasi *machine learning* *end-to-end* untuk memprediksi risiko kejadian gagal jantung (`DEATH_EVENT`) pada pasien berdasarkan 12 fitur rekam medis. Proyek ini mencakup seluruh alur pengembangan mulai dari eksplorasi data klinis, pemodelan berbasis **Random Forest**, hingga *deployment* aplikasi web interaktif menggunakan **Streamlit**.

🔗 **Live Demo:** `https://heart-failure-prediction-portfolio.streamlit.app/`  
🌐 **Portfolio Case Study:** `https://website-gamma-blue-30.vercel.app/`

---

## 📌 Project Overview

Penyakit kardiovaskular merupakan salah satu penyebab kematian tertinggi secara global, dengan gagal jantung sebagai komplikasi yang membutuhkan deteksi dini. Proyek ini bertujuan membangun alat bantu prediksi berbasis data klinis yang mampu mengklasifikasikan pasien ke dalam kategori **risiko rendah (`0`)** atau **risiko tinggi (`1`)** secara cepat dan mudah digunakan melalui antarmuka web.

**Sorotan Utama:**
- Menggunakan **12 variabel medis** terstruktur dari *UCI Machine Learning Repository*.
- Memanfaatkan model **Random Forest Classifier** (`trained_model_rf.pkl`) yang di-cache secara efisien menggunakan `@st.cache_resource` di Streamlit.
- Menyediakan antarmuka formulir medis yang terbagi menjadi 4 kategori logis lengkap dengan validasi input numerik dan indikator hasil berbasis warna.

---

## 📊 Dataset & Clinical Features

Model dilatih menggunakan *Heart Failure Clinical Records Dataset* dari **UCI Machine Learning Repository** dengan target klasifikasi biner `DEATH_EVENT` (`0` = Risiko Rendah / Bertahan, `1` = Risiko Tinggi).

Ke-12 fitur input dikelompokkan pada antarmuka aplikasi sebagai berikut:

| Kategori UI | Fitur | Deskripsi | Format / Nilai |
| :--- | :--- | :--- | :--- |
| **Identify Patient** | `age` | Usia pasien | Numerik (tahun) |
| | `anaemia` | Penurunan sel darah merah atau hemoglobin | Biner (`1` = Yes, `0` = No) |
| | `high_blood_pressure` | Riwayat hipertensi | Biner (`1` = Yes, `0` = No) |
| **Diagnosis** | `diabetes` | Riwayat penyakit diabetes | Biner (`1` = Yes, `0` = No) |
| | `ejection_fraction` | Persentase darah yang dipompa keluar jantung tiap kontraksi | Numerik (%) |
| **Blood Features** | `creatinine_phosphokinase` | Kadar enzim CPK dalam darah | Numerik (mcg/L) |
| | `platelets` | Jumlah trombosit dalam darah | Numerik (kiloplatelets/mL) |
| | `serum_sodium` | Kadar natrium serum dalam darah | Numerik (mEq/L) |
| **Patient Information** | `serum_creatinine` | Kadar kreatinin serum dalam darah | Numerik (mg/dL) |
| | `sex` | Jenis kelamin pasien | Biner (`1` = Male, `0` = Female) |
| | `smoking` | Status merokok pasien | Biner (`1` = Yes, `0` = No) |
| | `time` | Periode pemantauan (*follow-up period*) | Numerik (hari) |

---

## ⚙️ Machine Learning Workflow

1. **Data Acquisition & Exploration (EDA):** Memuat dataset UCI, memeriksa distribusi kelas `DEATH_EVENT`, anomali nilai, serta korelasi antar variabel medis.
2. **Data Preprocessing:** Menyiapkan fitur numerik dan biner, serta membagi data menjadi *training set* dan *testing set* (`[misal: 80:20]`).
3. **Model Training:** Melatih model klasifikasi **Random Forest** untuk menangani hubungan non-linear antar indikator medis sekaligus menghasilkan peringkat kepentingan fitur (*feature importance*).
4. **Evaluation & Serialization:** Mengevaluasi kinerja model pada data uji dan mengekspor model terbaik ke `trained_model_rf.pkl` menggunakan `joblib`.
5. **Deployment:** Mengintegrasikan model ke dalam aplikasi web interaktif `app.py` menggunakan **Streamlit**.

---

## 📈 Model Performance & Results

> *Catatan: Isi nilai metrik di bawah ini sesuai hasil evaluasi pada notebook pelatihan.*

| Metrik Evaluasi | Skor |
| :--- | :---: |
| **Accuracy** | `[77%]` |
| **Precision** | `[0.79]` |
| **Recall** | `[0.77]` |
| **F1-Score** | `[0.75]` |


---

## 🖥️ Application Preview

![Heart Failure Prediction App](assets/predict-heart.png)

Pengguna memasukkan 12 parameter klinis pada formulir, menekan **Click Here to Predict**, dan aplikasi langsung menampilkan status prediksi:
- 🟢 **Risiko Rendah (`0`):** Ditampilkan dengan notifikasi hijau (`st.success`).
- 🔴 **Risiko Tinggi (`1`):** Ditampilkan dengan notifikasi merah (`st.error`).

---

## 📂 Project Structure

```text
Heart-Failure-Prediction/
├── app.py                   # Aplikasi web Streamlit untuk inferensi real-time
├── trained_model_rf.pkl     # Model Random Forest yang telah dilatih
├── requirements.txt         # Daftar dependensi Python
├── notebooks/               # Eksplorasi data & notebook pelatihan model (sesuaikan nama file)
└── assets/                  # Screenshot aplikasi, diagram workflow, dan grafik evaluasi
