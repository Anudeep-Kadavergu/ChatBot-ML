import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_tutorial"    
)
mycursor = mydb.cursor()
sql = """select * from user where PO = %s"""
mycursor.execute(sql, ("PO123456",))
users = mycursor.fetchall()
s=""
for user in users:
    for i in user:
        s=s+str(i)
    
