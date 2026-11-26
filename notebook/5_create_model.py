from sklearn.preprocessing import StandardScaler
import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from joblib import dump

# Koneksi ke MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="HEART"
)

def fetch_data():
    try:
        # Query untuk mengambil data
        query = "SELECT * FROM heart_failure_table"
        # Gunakan pandas untuk membaca data ke dalam DataFrame
        df = pd.read_sql(query, mydb)
    finally:
        mydb.close()
    
    return df

# Ambil data dari database
data = fetch_data()
print("Data fetched from the database:")
print("Cek data:  ", data.head())

# Pisahkan fitur dan target variabel
X = data.drop(columns=['DEATH_EVENT', 'id'])  # Hapus kolom 'DEATH_EVENT' dan 'id'
y = data['DEATH_EVENT']

# Normalisasi fitur numerik
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model_rf = RandomForestClassifier()
model_svm = SVC()

model_rf.fit(X_train, y_train)
model_svm.fit(X_train, y_train)

# Make predictions on the test set
y_pred_rf = model_rf.predict(X_test)
y_pred_svm = model_svm.predict(X_test)

target_names = [0, 1]
# Evaluate the model
print("Random Forest", classification_report(y_test,y_pred_rf))
print("SVM", classification_report(y_test,y_pred_svm))

# Save the model to a file
model_filename_rf = 'trained_model_rf.pkl'
model_filename_svm = 'trained_model_svm.pkl'
dump(model_rf, model_filename_rf)
dump(model_svm, model_filename_svm)
print(f"Model saved to {model_filename_rf} and {model_filename_svm}")




