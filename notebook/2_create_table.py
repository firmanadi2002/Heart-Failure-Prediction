import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="HEART"
)


mycursor = mydb.cursor()

drop_table_if_exist = "DROP TABLE IF EXISTS heart_failure_table"

query = """CREATE TABLE heart_failure_table (
            id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            age INT NOT NULL,
            anaemia TINYINT NOT NULL,  -- TINYINT for boolean-like values
            creatinine_phosphokinase INT NOT NULL,
            diabetes TINYINT NOT NULL,  -- TINYINT for boolean-like values
            ejection_fraction INT NOT NULL,
            high_blood_pressure TINYINT NOT NULL,  -- TINYINT for boolean-like values
            platelets BIGINT NOT NULL,  -- BIGINT for large integer values like platelets
            serum_creatinine FLOAT NOT NULL,  -- Changed to FLOAT without size specification
            serum_sodium INT NOT NULL,
            sex TINYINT NOT NULL,  -- TINYINT for binary gender (0 or 1)
            smoking TINYINT NOT NULL,  -- TINYINT for boolean-like values
            time INT NOT NULL,
            DEATH_EVENT TINYINT NOT NULL)"""
  

mycursor.execute(drop_table_if_exist)
mycursor.execute(query)

print("heart table is created in the database")

mydb.commit()
mycursor.close()
mydb.close()
