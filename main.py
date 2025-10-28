from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    # Pega a mensagem que o usuário enviou
    incoming_msg = request.form.get("Body", "").strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    # Responde com base no conteúdo
    if "oi" in incoming_msg:
        msg.body("Oi! 👋 Tudo bem? Eu sou o seu bot do Replit com Twilio.")
    elif "tudo bem" in incoming_msg:
        msg.body("Tudo ótimo! E você?")
    else:
        msg.body("Desculpe, não entendi. Pode repetir?")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)