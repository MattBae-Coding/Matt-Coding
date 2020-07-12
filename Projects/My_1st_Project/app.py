from flask import Flask, render_template, request, jsonify
app = Flask(__name__) #flaks를 사용하겠다는 말

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('mongodb://test:test@localhost',27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

#HTML
@app.route('/') #5000 뒤에 붙는것
def home():
   return render_template('index.html')
@app.route('/enroll') #5000 뒤에 붙는것
def enroll():
   return render_template('enroll.html')


#API
@app.route('/save', methods=['POST'])
def save():
   name_get = request.form['name_give']
   dob_get = request.form['dob_give']
   diary_get = request.form['diary_give']

   doc = {
      'name':name_get,
      'dob':dob_get,
      'diary':diary_get
   }
   db.myproject.insert_one(doc)
   return jsonify({'result':'success', 'msg': '저장완료!!'})

@app.route('/show', methods=['POST'])
def show():
   name_get = request.form['name_give']
   dob_get = request.form['dob_give']
   diarys  = list(db.myproject.find({'name':name_get,'dob':dob_get},{'_id':0}))
   return jsonify({'result':'success', 'all_diarys':diarys})

#flaks를 돌려주는 친구 - 계속 돌아감  
if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True) 