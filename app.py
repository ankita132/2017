from flask import Flask
from flask_session import Session

app = Flask(__name__)
sess = Session()

@app.route('/', methods=['GET'])
def main():
    return "Coming soon!"


app.secret_key = 'kwoc'
app.config['SESSION_TYPE'] = 'filesystem'

sess.init_app(app)
app.debug = True

if __name__ == '__main__':
    app.run(debug=True)
