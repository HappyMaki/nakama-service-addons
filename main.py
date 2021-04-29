from gmail_util import send_email
from flask import Flask, request
app = Flask(__name__)

@app.route('/status')
def status():
    return "0"

@app.route('/send_verification')
def send_verification():
    to_email = request.args.get('email')
    send_email(to_email)
    return to_email



if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

