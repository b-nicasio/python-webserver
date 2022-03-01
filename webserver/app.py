from flask import Flask, render_template, redirect, request
from database_operations import insert, count_rows
from flaskext.mysql import MySQL
import names
from decouple import config

app = Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']=config('DB_HOST')
app.config['MYSQL_DATABASE_USER']=config('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD']=config('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB']=config('DB_DATABASE')
mysql.init_app(app)

@app.route('/')
def index():
    return redirect("/greeting")

@app.route('/greeting')
def greeting():
    (row_count,data) = count_rows(mysql)
    print(data)
    print(type(data))
    return render_template('index.html', data=data, row_count=row_count)

@app.route('/messages', methods=['POST'])
def post_to_database():
    random_name = names.get_first_name()
    name = insert(mysql, random_name)
    return render_template('messages.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', url=request.url_root), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
