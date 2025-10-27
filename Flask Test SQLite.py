import sqlite3 as sql

conn = sql.connect('database.db')
#print ("Opened Database Successfully")

#query = 'CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)'
#query = "INSERT INTO students (name, addr, city, pin) \
#        VALUES ('Melvic', 'Trece', 'Trece', '4109')"

#conn.execute (query)
#conn.commit()
query = "SELECT * FROM students"
cursor = conn.execute (query)

for row in cursor:
    print ("Name = ", row[0])
    print ("Address = ", row[1])
    print ("City = ", row[2])
    print ("Pin = ", row[3])


#print ("Table Created Successfully")
conn.close()