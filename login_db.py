import cgi
import mysql.connector

form = cgi.FieldStorage()
first_name = form.getvalue("first_name")
last_name = form.getvalue("last_name")
student_num = form.getvalue("student_num")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="AttendScan_DB"
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    student_num CHAR(7) NOT NULL
)
""")

cursor.execute(
    "INSERT INTO students (first_name, last_name, student_num) VALUES (%s, %s, %s)",
    (first_name, last_name, student_num)
)

conn.commit()

cursor.close()
conn.close()