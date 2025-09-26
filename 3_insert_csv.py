import mysql.connector
import pandas as pd
import numpy as np

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="HEART"
)

mycursor = mydb.cursor()

# Prepare the SQL query for insertion
query = """INSERT INTO heart_failure_table (age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time, DEATH_EVENT) 
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Load data from the CSV file
data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

# Convert all numerical columns to native Python float
# Explicitly cast any numpy.float64 to Python float
data = data.applymap(lambda x: float(x) if isinstance(x, (np.float64, np.float32)) else x)

# Handle missing values (NaN) - here we're filling NaNs with 0, but you can also drop them
data = data.fillna(0)

# Convert each row to a tuple of native Python float for all columns
values_to_insert = []
for index, row in data.iterrows():
    values_to_insert.append((
        float(row['age']),  # Ensure 'age' is a float
        int(row['anaemia']),  # Ensure 'anaemia' is an integer (or TINYINT in MySQL)
        int(row['creatinine_phosphokinase']),
        int(row['diabetes']),
        int(row['ejection_fraction']),
        int(row['high_blood_pressure']),
        int(row['platelets']),
        float(row['serum_creatinine']),  # Ensure 'serum_creatinine' is a float
        int(row['serum_sodium']),
        int(row['sex']),
        int(row['smoking']),
        int(row['time']),
        int(row['DEATH_EVENT'])  # Ensure 'DEATH_EVENT' is an integer (or TINYINT in MySQL)
    ))

# Execute batch insert
mycursor.executemany(query, values_to_insert)

# Commit the transaction
mydb.commit()

# Close the cursor and database connection
mycursor.close()
mydb.close()

print("Data has been successfully inserted into the database!")
