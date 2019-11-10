from flask import Flask, request
from salt import Salt
from enc import Pass

app = Flask(__name__)


@app.route("/salt", methods=['POST'])
def hello():
    print((request.get_json()))
    bodyParams = request.get_json()
    if not bodyParams['key']:
        return "Missing parameter or wrong parameter provided."

    Salt.save_salt(Salt, bodyParams['key'])
    return "Salt Generated"


@app.route("/salt", methods=['GET'])
def hello2():
    print((request.get_json()))
    bodyParams = request.get_json()
    if not bodyParams['key']:
        return "Missing parameter or wrong parameter provided."
    return str(Salt.decrypt_salt(Salt, bodyParams['key']))


@app.route("/password", methods=['POST'])
def hello2():
    print((request.get_json()))
    bodyParams = request.get_json()
    if not bodyParams['key']:
        return "Missing parameter or wrong parameter provided."
    return str(Salt.decrypt_salt(Salt, bodyParams['key']))




if __name__ == "__main__":
    app.run()