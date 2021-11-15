from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return 'Hello!'

app.run(host='0.0.0.0', port=8000)

