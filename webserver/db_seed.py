from database_operations import mysql

# Inserting first data
conn = mysql.connect()
cursor = conn.cursor()
# Create insert name into table names
sql = "INSERT INTO names (name) VALUES ('Bernie');"
cursor.execute(sql)
conn.commit()
print("Database seed completed")
