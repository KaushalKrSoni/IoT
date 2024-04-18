# imported dbconn to import mysql connector

import dbconn

# to create a query
empid = int(input("Enter empid: "))
name = input("Enter Name: ")
department = input("Enter department: ")
email = input("Enter email: ")
salary = float(input("Enter salary: "))
date_of_joining = input("Enter date_of_joining: ")

conn = dbconn.get_connection()

query = f"insert into employees values({empid}, '{name}', '{department}', '{email}', {salary}, '{date_of_joining}');"

# create a cursor to execure the query
cursor = conn.cursor()

# execute query using cursor
cursor.execute(query)

# after execution of query commit your changes
conn.commit()

# close the cursor and connection
cursor.close()
conn.close()