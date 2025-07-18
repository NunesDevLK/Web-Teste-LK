from flask import Flask, render_template_string, request

app = Flask(__name__)

chat_log = []

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>IA do Nunes</title>
    <style>
        body { font-family: Arial, sans-serif; background: #1e1e1e; color: #fff; padding: 20px; }
        .chat-box { border: 1px solid #444; border-radius: 10px; padding: 10px; background: #2b2b2b; max-width: 600px; margin: auto; }
        .msg { margin: 10px 0; }
        .user { color: #4fc3f7; }
        .ia { color: #a5d6a7; }
        form { margin-top: 20px; display: flex; }
        input[type=text] { flex: 1; padding: 10px; border: none; border-radius: 5px; }
        button { padding: 10px; border: none; background: #4fc3f7; color: #000; border-radius: 5px; margin-left: 10px; }
    </style>
</head>
<body>
    <div class="chat-box">
        <h2>IA do Nunes 🤖</h2>
        {% for msg in chat %}
            <div class="msg"><strong class="user">Você:</strong> {{ msg['pergunta'] }}</div>
            <div class="msg"><strong class="ia">IA:</strong> {{ msg['resposta'] }}</div>
        {% endfor %}
        <form method="post">
            <input type="text" name="pergunta" placeholder="Fale com a IA..." autocomplete="off" required>
            <button type="submit">Enviar</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pergunta = request.form["pergunta"]
        resposta = responder(pergunta)
        chat_log.append({"pergunta": pergunta, "resposta": resposta})
    return render_template_string(HTML, chat=chat_log)

def responder(pergunta):
    pergunta = pergunta.lower()
    if "oi" in pergunta:
        return "Olá! Como posso te ajudar hoje?"
    elif "tudo bem" in pergunta:
        return "Sim! Estou funcionando a todo vapor 😄"
    elif "quem é você" in pergunta:
        return "Sou a IA do Nunes, criada no celular com muito estilo 🚀"
    elif "adeus" in pergunta:
        return "Tchau! Foi bom conversar com você 👋"
    else:
        return "Desculpa, ainda estou aprendendo. Pode perguntar de outro jeito?"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
