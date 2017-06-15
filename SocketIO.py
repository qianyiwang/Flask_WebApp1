from flask.ext.socketio import SocketIO, emit
rom flask import Flask, render_template, request, json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('my event')
def test_message(message):
	emit('my response', {'data': 'got it!'})

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('socket.html')
 
@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')
 
    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print "Starting Thread"
        thread = RandomThread()
        thread.start()

if __name__ == "__main__":
    socketio.run(app)