from flask import Flask, render_template, redirect, request, session, url_for
from app.functions import get_auth_url, get_token

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "your-very-secret-key"

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login")
def login():
    if session.get("token_info"):
        return redirect(url_for("home"))
    
    auth_url = get_auth_url()
    return render_template("login.html", auth_url=auth_url)

@app.route("/logging_in")
def logging_in():
    code = request.args.get("code")
    if code:
        token_info = get_token(code)
        session["token_info"] = token_info
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))

@app.route("/home")
def home():
    if not session.get("token_info"):
        return redirect(url_for("login"))
    
    return render_template("home.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
