from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
import os

app = Flask(__name__)
client_openai = OpenAI()

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    # Pega a mensagem e número do usuário
    mensagem_usuario = request.form.get("Body", "")
    numero_usuario = request.form.get("From", "")

    print(f"Mensagem recebida de {numero_usuario}: {mensagem_usuario}")

    # Gera a resposta com o ChatGPT
    try:
        completion = client_openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente simpático e direto, estilo Alexa."},
                {"role": "user", "content": mensagem_usuario}
            ]
        )
        resposta_chatgpt = completion.choices[0].message.content
    except Exception as e:
        print("Erro com a API da OpenAI:", e)
        resposta_chatgpt = "Ops! Tive um erro interno. Tente novamente mais tarde."

    # Cria resposta TwiML
    twiml = MessagingResponse()
    twiml.message(resposta_chatgpt)

    # Retorna a resposta como XML
    return Response(str(twiml), mimetype="application/xml")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
