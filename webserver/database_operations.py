def insert(mysql, value):
    sql = f"insert into names (name) values('{value}');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)

    # Get last inserted name ID
    last_id = str(cursor.lastrowid)
    print(last_id)
    conn.commit()
    print("sending value" + last_id)
    return select_value(mysql, last_id)

def select_value(mysql, value):
    print("here2 = " + value)
    print(f"select from names where id='{value}';")
    sql = f"select * from names where id='{value}';"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    names=cursor.fetchone()
    print("Printing the select:")
    print(names)
    conn.commit()
    return names

def count_rows(mysql):
    sql = 'select COUNT(*) from names;'
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    names=cursor.fetchone()

    sql = 'select * from names ORDER BY id DESC LIMIT 10;'
    cursor.execute(sql)
    data=cursor.fetchall()
    print(names)
    conn.commit()
    return (names, data)

def migration(mysql):
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "create table names(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"
    cursor.execute(sql)

def seed(mysql):
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "create table names(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"
    cursor.execute(sql)
