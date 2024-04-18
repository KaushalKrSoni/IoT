import dbconn

conn = dbconn.get_connection()

query = "select * from employees order by salary ASC;"

cursor = conn.cursor()
cursor.execute(query)

records = cursor.fetchall()

print(records)

cursor.close()
conn.close()