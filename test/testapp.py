from flask import Flask, request, flash, redirect, url_for, render_template
from flask_pymongo import PyMongo
from dateutil.parser import parse
import datetime


app = Flask(__name__)

app.secret_key = 'secret'


# app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/testdb'
# app.config['MONGO_URI'] = 'mongodb://192.168.99.100:27017/testdb'
# app.config['MONGO_URI'] = 'mongodb://18.183.180.241:27017/testdb'

# ECS用
# app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/testdb'

# mongoDBサーバ(EC2)用
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/testdb'

mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def show_entry():
    entries = []
    users = mongo.db.user.find()
    today = datetime.date.today().strftime('%Y/%m/%d')

    for row in users:
        entries.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})

    return render_template('toppage.html', currentDate=today)


@app.route('/add', methods=['POST'])
def add_entry():
    mongo.db.user.insert({"name": request.form['name'], "birthday": parse(request.form['birthday'])})
    flash('New entry was successfully posted')

    return redirect(url_for('show_entry'))


@app.route('/search', methods=['POST'])
def filter_entry():
    results = []

    start = parse(request.form['start'])
    end = parse(request.form['end'])

    cur = mongo.db.user.find({'birthday': {'$lt': end, '$gte': start}})

    for row in cur:
        results.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})

    return render_template('result.html', results=results)

@app.route('/historyDetail', methods=['GET'])
def show_detail():
    return render_template('historyDetail.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
