from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/api', methods=["POST"])
def calcula_imc():
    resp = request.get_json()
    peso, altura = resp["peso"], resp["altura"]
    resultado = round(peso / altura ** 2, 2)
    return jsonify({"resultado":resultado})

@app.after_request
def add_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Content-Type,Authorization")
    return response


if __name__ =="__main__":
    app.run()
