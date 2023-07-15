import socketio

sio = socketio.Client()


@sio.event
def connect():
    handle_event()


@sio.event
def disconnect():
    print("Connection Ended.")


def handle_event():
    print("Connection Successful.")


@sio.event
def connection_error():
    print("Oops! Something went wrong.")