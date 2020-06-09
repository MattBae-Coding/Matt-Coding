from flask import Flask
app = Flask(__name__)

@app.route('/') #5000 뒤에 붙는것
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage(): #의미 없음 겹치지만 않으면 됨
   return 'This is mypage!'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True) #flaks를 돌려주는 친구 - 계속 돌아감 
