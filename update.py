# to import connection, import dbconn

import dbconn

def update_employees(empid, salary):
    conn = dbconn.get_connection()

    query = f"update employees SET salary = %s where empid = %s;"
    val = (salary, empid)

    cursor = conn.cursor()

    cursor.execute(query, val)
    conn.commit()

    cursor.close()
    conn.close()

update_employees(65, 95432)