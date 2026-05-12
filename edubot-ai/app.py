from flask import Flask, render_template, request, jsonify
from groq import Groq

# API KEY GROQ
client = Groq(
    api_key="api_key"
)

app = Flask(__name__)

chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        user_message = data["message"]

        # simpan history
        chat_history.append({
            "role": "user",
            "content": user_message
        })

        # request AI
        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",
            
            messages=chat_history
        )

        bot_reply = response.choices[0].message.content

        # simpan balasan
        chat_history.append({
            "role": "assistant",
            "content": bot_reply
        })

        return jsonify({
            "reply": bot_reply
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "reply": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(debug=True)