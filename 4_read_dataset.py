import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="HEART"
)


mycursor = mydb.cursor()

query = "SELECT * FROM heart_failure_table"
  


mycursor.execute(query)

results = mycursor.fetchall()

for row in results:
   print(row)


mydb.commit()
mycursor.close()
mydb.close()