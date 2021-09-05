import base64

def __init__(msg):
    decoded = base64.b64decode(msg)
    return decoded
