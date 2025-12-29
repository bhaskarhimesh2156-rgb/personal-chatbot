from google import genai
from flask import Flask,request,jsonify,render_template
client=genai.Client(api_key='YOUR_APIKEY')
app= Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():
    # Get user message from request
    prompt = request.json["message"]

    # Send prompt to Gemini model
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Return model response
    return jsonify({"reply": response.text})

app.run(port=8080)
