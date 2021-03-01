import sqlite3
conn = sqlite3.connect("test_login.db")
#command = """ create table user_login 
#(name text, user_id text, password text, phone text, email_id text)
#"""
command = '''insert into user_login(name, user_id, password, phone, 
email_id) values ("shoeb ahmed", "shoeb370", "shoeb123", "+917303764284",
"shoebahmed370@gmail.com")
'''
conn.execute(command)
print("table created")
conn.commit()
conn.close()