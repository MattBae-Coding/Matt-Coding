from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    #1. 전달받은 데이터를 꺼낸다.
    title = request.form['title_give']
    review = request.form['review_give']
    author = request.form['author_give']
    #2. 그걸 DB에 잘 저장한다.
    doc = {
        'title':title,
        'review':review,
        'author':author,
    }
    db.reviews.insert_one(doc)
    #3. 잘 저장했다고 대답해준다.
    return jsonify({'result':'success', 'msg': '리뷰가 성공적으로 작성 되었습니다.'})


@app.route('/reviews', methods=['GET'])
def read_reviews():  
    #1. 기존 리뷰 내용을 검색해서 가져온다
    # db.reviews.find({찾을조건},{필요없는 녀석기록})
    reviews = list(db.reviews.find({},{'_id': False}))
    return jsonify({'result':'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)