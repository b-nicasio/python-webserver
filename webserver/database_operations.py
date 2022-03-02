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

def insert(value):
    sql = f"insert into names (name) values('{value}');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    last_id = str(cursor.lastrowid) # <- Get last inserted name ID
    print(last_id)
    conn.commit()
    print("sending value" + last_id)
    return select_value(last_id)


def select_value(value):
    sql = f"select * from names where id='{value}';"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    names = cursor.fetchone() # <- Store name value
    print("Printing the select:")
    print(names)
    conn.commit()
    return names

def count_rows():
    sql = 'select COUNT(*) from names;'
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchone() # <- Store row count
    sql = 'select * from names ORDER BY id DESC LIMIT 10;'
    cursor.execute(sql)
    data = cursor.fetchall() # <- Store all names
    conn.commit()
    return (rows, data)
