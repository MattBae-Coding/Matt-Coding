from flask import Flask, render_template, request, jsonify
app = Flask(__name__) #flaks를 사용하겠다는 말
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
   return jsonify({'result':'success', 'msg': '저장완료'})

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


#flaks를 돌려주는 친구 - 계속 돌아감 
if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True) 