from flask import Flask, render_template, request, jsonify
app = Flask(__name__) #flaks를 사용하겠다는 말

@app.route('/') #5000 뒤에 붙는것
def home():
   return render_template('index.html')

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True) #flaks를 돌려주는 친구 - 계속 돌아감 ip