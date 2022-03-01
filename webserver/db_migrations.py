from flask import Flask
from flaskext.mysql import MySQL
from decouple import config

app = Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']=config('DB_HOST')
app.config['MYSQL_DATABASE_USER']=config('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD']=config('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB']=config('DB_DATABASE')
mysql.init_app(app)

# Creating tables
conn = mysql.connect()
cursor = conn.cursor()
sql = "CREATE TABLE IF NOT EXISTS names(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"
cursor.execute(sql)
conn.commit()
print("Migrations completed")
