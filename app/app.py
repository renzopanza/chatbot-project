from flask import Flask, render_template, request, redirect, url_for, session
from main import gerar_resposta
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
app.secret_key = "chatbook_secret"  # Necessário para uso da sessão


@app.route("/", methods=["GET", "POST"])
def index():
    if "historico" not in session:
        session["historico"] = []

    if request.method == "POST":
        user_message = request.form["message"]

        # Gera resposta usando o backend
        resposta_bot = gerar_resposta(user_message)

        # Atualiza histórico na sessão
        historico = session["historico"]
        historico.append({"user": user_message, "bot": resposta_bot})
        session["historico"] = historico

        return redirect(url_for("index"))

    return render_template("index.html", historico=session["historico"])


@app.route("/resetar")
def resetar():
    session.pop("historico", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
