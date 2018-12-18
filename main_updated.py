from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return 'Hello World!'
    else:
        subprocess.call(['/home/yuqi_tu/updateGitRepoByWebhook.sh'])
        return '{"status":"received"}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
