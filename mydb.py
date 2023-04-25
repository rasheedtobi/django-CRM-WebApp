import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='rasheed'
)

cusrorObject = dataBase.cursor()

cusrorObject.execute("CREATE DATABASE nacho")

print("All set")
