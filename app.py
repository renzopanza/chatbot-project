from flask import Flask, render_template, request, jsonify
from chatBot import obter_resposta

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def index():
    msg_boas_vindas = "Olá! Como posso te ajudar hoje? Qual gênero literário você procura?"
    return render_template("index.html", msg_boas_vindas=msg_boas_vindas)

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    user_message = data.get("message")
    if not user_message:
        return jsonify({"response": "Por favor, envie uma mensagem válida."})

    bot_response = obter_resposta(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
