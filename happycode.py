"""  MySQLdb """
import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='localhost', database='pydb')
mycursor = conn.cursor()

while 1:
    def MySQLVname():
        mycursor.execute("SHOW VARIABLES LIKE '%version%' ")
        print mycursor.fetchall()

    def dbName():
        mycursor.execute("SELECT DATABASE()")
        print mycursor.fetchall()

    def tableNames():
        mycursor.execute("SHOW TABLES")
        print mycursor.fetchall()


    def RetData():
        tname = input("Enter Table Name:")
        mycursor.execute("SELECT * FROM %s" % str(tname))
        print mycursor.fetchall()


    def CreateTable():
        Tablename = input("Enter New Table Name:")
        mycursor.execute("SHOW TABLES")
        tablen = mycursor.fetchall()
        if Tablename not in tablen:
                noOfColumns = input("Enter number of columns you want:")
                print "k good %d columns and constraints you want to give" % int(noOfColumns)
                for i in noOfColumns:
                    col1 = input("Enter Column Name:")
                    Datatype = input("Enter datatype:")
                    length = input("Enter length:")
            mycursor.execute("CREATE TABLE %s" % Tablename)
            conn.commit()
            print "Successfully created the table"
        else:
            print "Table already exist in pydb Database"

    def insertData(name,age,email,address):
        mycursor.execute(
            "INSERT INTO record(NAME,AGE,EMAIL,ADDRESS) VALUES('%s',%d,'%s','%s')" % (name, age, email, address)
        )
        conn.commit()
        print "Data Successfully Inserted"

    v = input("Enter the function name you want:")
