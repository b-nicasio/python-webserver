from flask import Flask, render_template, redirect, request
from database_operations import insert, count_rows
import names

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/greeting")


@app.route('/greeting')
def greeting():
    (row_count, data) = count_rows()
    print(data)
    print(type(data))
    return render_template('index.html', data=data, row_count=row_count)


@app.route('/messages', methods=['POST'])
def post_to_database():
    random_name = names.get_first_name()
    name = insert(random_name)
    return render_template('messages.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
