from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
import os

app = Flask(__name__)
app.secret_key = "AIzaSyCZhmN1ayK0Fqb9jesJd2W4uVNxP2IQY4o" 

GENAI_API_KEY = "AIzaSyCZhmN1ayK0Fqb9jesJd2W4uVNxP2IQY4o"
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_response(pet, text, user_id):
    if "chat_history" not in session:
        session["chat_history"] = {}
        print("Initialized chat_history in session.")  # 添加日志，確保這裡有執行
def generate_response(pet, text, user_id):
    if "chat_history" not in session:
        session["chat_history"] = {}

    if user_id not in session["chat_history"]:
        session["chat_history"][user_id] = []  

    session["chat_history"][user_id].append(f"主人：{text}")

    chat_context = "\n".join(session["chat_history"][user_id])
    prompt = f"你是一隻{'快樂的小狗狗名字叫麻吉' if pet == 'dog' else '驕傲的貓咪名字叫米菲'}，並且會依照設定的個性簡單回答主人的問題。\n以下是與主人的對話：\n{chat_context}\nAI 回應："

    response = model.generate_content(prompt).text.strip()

    session["chat_history"][user_id].append(f"AI：{response}")

    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_response', methods=['POST'])
def generate():
    data = request.get_json()
    text = data['text']
    pet = data['pet']
    user_id = request.remote_addr 

    response = generate_response(pet, text, user_id)

    return jsonify({'response': response, 'pet': pet})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
