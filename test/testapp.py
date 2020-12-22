from flask import Flask, request, flash, redirect, url_for, render_template
from flask_pymongo import PyMongo
from dateutil.parser import parse
import datetime


app = Flask(__name__)

app.secret_key = 'secret'

# mongoDBサーバ設定（ECS用）
# app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/testdb'

# mongoDBサーバ設定（ローカル用）
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/testdb'

mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def show_entry():
    # 参照機能は追って追加予定（'''部分はコメントアウト）
    '''
    entries = []
    users = mongo.db.user.find()


    for row in users:
        entries.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})
    '''

    today = datetime.date.today().strftime('%Y/%m/%d')

    return render_template('toppage.html', currentDate=today)


@app.route('/add', methods=['POST'])
def add_entry():
    '''登録機能実装↓'''

    # 登録フォームの内容をそれぞれ変数に格納
    billName = request.form['bills']
    workingDay = parse(request.form['workingDay'])
    temperature = request.form['temperature']
    # params = request.form['params']

    # print(params)


    # mongoDBに登録
    mongo.db.base.insert_one({"billName": billName, "workingDay": workingDay, "temperature": temperature})

    # 登録完了後にフラッシュメッセージ生成
    flash('New entry was successfully posted')

    # 登録TOP画面にリダイレクト
    return redirect(url_for('show_entry'))


@app.route('/search', methods=['POST'])
def filter_entry():
    # 検索機能は追って追加予定
    '''
    results = []

    start = parse(request.form['start'])
    end = parse(request.form['end'])

    cur = mongo.db.user.find({'birthday': {'$lt': end, '$gte': start}})

    for row in cur:
        results.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})

    return render_template('result.html', results=results)
    '''

@app.route('/historyDetail', methods=['GET'])
def show_detail():
    return render_template('historyDetail.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
