from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'db sparta' 라는 이름의 db를 만듭니다.


# HTML 을 주는 부분
@app.route('/')
def home():
    return render_template('shopping.html')


# API 역할을 하는 부분
@app.route('/shopping', methods=['POST'])
def ordering():
    name = request.form['name']
    count = request.form['count']
    address = request.form['address']
    phone = request.form['phone']
    doc = {
        'name': name,
        'count': count,
        'address': address,
        'phone': phone
    }
    db.shopping.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다!'})


@app.route('/shopping', methods=['GET'])
def read_order_list():
    shopping = list(db.shopping.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'msg': '현재 주문목록을 가져왔습니다!', 'shopping': shopping})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
