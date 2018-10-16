from flask import Flask, request, jsonify

app = Flask(__name__)

# GET
@app.route('/')
def hello():
    return "Hello World"

#running web app in local machine
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
	#One can use either 127.0.0.1 or localhost ip to access this webpage