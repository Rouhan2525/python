import sqlite3
conn = sqlite3.connect('std1.db')
cursor = conn.cursor()
table = """CREATE TABLE IF NOT EXISTS STUDENT (
            NAME VARCHAR(255),
            CLASS VARCHAR(255),
            SELECTION VARCHAR(255)
        );"""
cursor.execute(table)

cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SELECTION) VALUES ('ishan', '7th', 'A')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SELECTION) VALUES ('Aahil', '8th', 'B')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SELECTION) VALUES ('Aliya', '5th', 'C')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SELECTION) VALUES ('Hasan', '9th', 'D')")

print("Data inserted in the table")

cursor.execute("SELECT * FROM STUDENT")
data = cursor.fetchall()
for row in data:
    print(row)

conn.commit()
conn.close()
