import logging
from flask import Flask
app = Flask(__name__)

@app.rout('/')
def hell():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
