from database_operations import mysql

# Creating tables
conn = mysql.connect()
cursor = conn.cursor()
# Create table name with auto increment ID and automatic timestamp
sql = "CREATE TABLE IF NOT EXISTS names(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"
cursor.execute(sql)
conn.commit()
print("Migrations completed")
