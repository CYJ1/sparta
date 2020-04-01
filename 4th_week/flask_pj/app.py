from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'db sparta' 라는 이름의 db를 만듭니다.


# HTML 을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    title = request.form['title']
    author = request.form['author']
    review = request.form['review']
    doc = {
        'title': title,
        'author': author,
        'review': review
    }
    # 2. DB에 정보 삽입하기
    db.reviews.insert_one(doc)
    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다!'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    # 1. DB 에서 리뷰 정보 모두 가져오기
    reviews = list(db.reviews.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'msg': '현재 작성된 리뷰를 받아왔습니다!', 'reviews': reviews})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
