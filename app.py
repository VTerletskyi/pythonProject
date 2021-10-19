from flask import Flask

from main import read_data

app = Flask(__name__)


@app.route('/<company>')
def hello_world(company):
    data = read_data(company)
    return f"{data}"

# http://127.0.0.1:5000/PD


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
