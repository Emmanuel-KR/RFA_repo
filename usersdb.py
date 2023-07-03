import sqlite3
conn = sqlite3.connect('Users.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM cred")
#cursor.execute("INSERT INTO cred(Username, Password) VALUES(?, ?)",('Admin', '1234'))
#conn.commit()
#conn.close()
records = cursor.fetchall()
for record in records:
    print(record)