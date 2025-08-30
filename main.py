from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("loginpage.html")

# SOS page
@app.route("/sos")
def sos():
    return render_template("sos.html")   # 🚨 new SOS page

# API endpoint to receive SOS alerts
@app.route("/send_sos", methods=["POST"])
def send_sos():
    data = request.json
    latitude = data.get("lat")
    longitude = data.get("lon")

    # For now just print the alert
    print(f"🚨 SOS received! Location: {latitude}, {longitude}")

    return jsonify({"status": "success", "message": "SOS alert received!"})


if __name__ == "__main__":
    app.run(debug=True)
