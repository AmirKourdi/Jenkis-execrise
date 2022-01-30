import os
from flask import Flask
import socket
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/DOCKER')
def hello():
    docker_short_id = str(socket.gethostname())
    return docker_short_id

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
