"""  MySQLdb in python """
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
                print "k good, Give the column details"
                templist = " "
                finallist = []
                for i in range(noOfColumns):
                    if i == noOfColumns-1:
                        s = ' '
                    else:
                        s = ', '
                    colname = input("Enter Column Name:")
                    templist += colname + ' '
                    Datatype = input("Enter datatype:")
                    templist +=  Datatype + ' '
                    length = input("Enter length:")
                    templist +=  '(' + length + ')' + s
                finallist.append(templist)
                str1 = " ".join(finallist)
                mycursor.execute("CREATE TABLE %s (%s)" % (Tablename, str1))
                conn.commit()
                print "Successfully created the table"
        else:
            print "Table already exist in pydb Database"

    def insertData():
        tname = input("Enter Table Name:")
        mycursor.execute("DESCRIBE %s" % tname)
        print mycursor.fetchall()

        # mycursor.execute(
        #     "INSERT INTO tname(NAME,AGE,EMAIL,ADDRESS) VALUES('%s',%d,'%s','%s')" % (name, age, email, address)
        # )
        conn.commit()
        print "Data Successfully Inserted"

    v = input("Enter the function name you want:")
