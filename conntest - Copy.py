import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="darshan_ece"  
)
print("connected to the data batabase successfully")