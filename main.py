from flask import Flask, render_template, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials
ACCOUNT_SID = ""
AUTH_TOKEN = ""
TWILIO_PHONE = "+"         # Your Twilio phone number for SMS
TWILIO_WHATSAPP = ""  # Twilio Sandbox WhatsApp number
EMERGENCY_CONTACT = ""  # Replace with your verified number
EMERGENCY_WHATSAPP = ""

# Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("loginpage.html")

@app.route("/sos")
def sos():
    return render_template("sos.html")

@app.route("/resource")
def resource():
    return render_template("resource.html")

@app.route("/send_sos", methods=["POST"])
def send_sos():
    data = request.json
    latitude = data.get("lat")
    longitude = data.get("lon")

    # Create alert message
    message_text = f"🚨 SOS Alert!\nLocation: https://www.google.com/maps?q={latitude},{longitude}"

    try:
        # Send SMS
        client.messages.create(
            body=message_text,
            from_=TWILIO_PHONE,
            to=EMERGENCY_CONTACT
        )

        # Send WhatsApp
        client.messages.create(
            body=message_text,
            from_=TWILIO_WHATSAPP,
            to=EMERGENCY_WHATSAPP
        )

        print("✅ SOS sent via SMS & WhatsApp!")
        return jsonify({"status": "success", "message": "SOS alert sent via SMS & WhatsApp!"})
    except Exception as e:
        print(f"❌ Error sending SOS: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
