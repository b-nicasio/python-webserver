from flask import Flask
from flaskext.mysql import MySQL
from decouple import config

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = config('DB_HOST')
app.config['MYSQL_DATABASE_USER'] = config('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = config('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = config('DB_DATABASE')
mysql.init_app(app)

# Inserting first data
conn = mysql.connect()
cursor = conn.cursor()
sql = "INSERT INTO names (name) VALUES ('Bernie');"
cursor.execute(sql)
conn.commit()
print("Database seed completed")
