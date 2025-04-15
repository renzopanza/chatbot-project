from flask import Flask, render_template, request, session, redirect, url_for
from chatBot import gerar_resposta

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "chave-secreta-super-segura"  # Requerido para usar sessões

@app.route("/", methods=["GET", "POST"])
def index():
    # Adiciona mensagem inicial se for a primeira visita
    if "historico" not in session:
        session["historico"] = [
            {"user": "", "bot": "Olá! Como posso te ajudar hoje?"}
        ]

    if request.method == "POST":
        mensagem = request.form["message"]
        resposta = gerar_resposta(mensagem)

        # Adiciona a nova troca ao histórico
        session["historico"].append({"user": mensagem, "bot": resposta})
        session.modified = True  # Informa ao Flask que a sessão foi alterada

        return redirect(url_for("index"))  # Redireciona para evitar reposts em refresh

    return render_template("index.html", historico=session["historico"])

@app.route("/resetar")
def resetar():
    session.pop("historico", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
