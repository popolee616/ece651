from flask import Flask, request, jsonify

app = Flask(__name__)

# GET
@app.route('/')
def hello():
    return "Hello World"

@app.route('/register',methods=['POST'])
def register():
    content = request.json

    print(content['userName'])
    print(content['userPassword'])
    print(content['userEmail'])
    return "Register successfully!\t Welcome " + content['userName']
#running web app in local machine
if __name__=='__main__':
    #http://127.0.0.1:5000/
    app.run(host='0.0.0.0', port=5000)