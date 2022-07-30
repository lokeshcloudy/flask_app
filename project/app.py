from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socket_ = SocketIO(app)

@app.route('/')
def indux():
    return render_template('index.html', name="2.2.2")


if __name__ == '__main__':
    socket_.run(app, debug=True)
