import mysql.connector
# from HTMLParser import HTMLParser
from dominate.tags import *

conn = mysql.connector.connect(user='root', password='', host='localhost', database='pydb')
mycursor = conn.cursor()
while (1):
    Val = input("\t\t\t\tEnter 1: Show Mysql Version \n \
				Enter 2: Show Selected Database Name \n \
				Enter 3: Show available Tables \n \
				Enter 4: See the table data \n \
				Enter 5: To Exit \n \
				Your Option:")
    if Val == 1:
        mycursor.execute("SHOW VARIABLES LIKE '%version%' ")
    elif Val == 2:
        mycursor.execute("SELECT DATABASE()")
    elif Val == 3:
        mycursor.execute("SHOW TABLES")
    elif Val == 4:
        """tdb = input("Enter database name:")
        mycursor.execute("USE %s" % str(tdb))
        mycursor.execute("SHOW TABLES")
        print(mycursor.fetchall())"""
        tname = input("Enter Table Name:")
        mycursor.execute("SELECT * FROM %s" % str(tname))
    elif Val == 5:
        break
    else:
        print H1("ERROR::Enter Valid number please")

    print(mycursor.fetchall())
