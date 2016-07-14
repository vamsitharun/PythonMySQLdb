import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='localhost', database='pydb')
mycursor = conn.cursor()

def MySQLVname():
    mycursor.execute("SHOW VARIABLES LIKE '%version%' ")
    print mycursor.fetchall()

def dbname():
    mycursor.execute("SELECT DATABASE()")
    print mycursor.fetchall()

v = input("Enter the function name you want:")
