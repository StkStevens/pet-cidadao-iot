
from flask import Flask, request, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "projeto": "PET CIDADAO",
        "status": "API Flask funcionando"
    })


@app.route("/identificar", methods=["POST"])
def identificar():

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({
            "sucesso": False,
            "mensagem": "JSON invalido"
        }), 400

    uid = dados.get("uid")
    dispositivo = dados.get("dispositivoId")

    if not isinstance(uid, str) or not uid.strip():
        return jsonify({
            "sucesso": False,
            "mensagem": "UID obrigatorio"
        }), 400

    if not isinstance(dispositivo, str) or not dispositivo.strip():
        return jsonify({
            "sucesso": False,
            "mensagem": "Dispositivo obrigatorio"
        }), 400

    uid = uid.strip().upper()
    dispositivo = dispositivo.strip()

    print("ANIMAL IDENTIFICADO:", uid, flush=True)

    return jsonify({
        "sucesso": True,
        "mensagem": "Identificacao recebida",
        "uid": uid,
        "dispositivoId": dispositivo,
        "recebidoEm": datetime.now(timezone.utc).isoformat()
    }), 200


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
