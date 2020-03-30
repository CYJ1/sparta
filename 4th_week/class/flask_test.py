from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'This is Home!'


@app.route('/mypage')
def mypage():
    return 'This is My Page!'


@app.route('/mypage2')
def mypage2():
    return 'This is My Page2!'


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
