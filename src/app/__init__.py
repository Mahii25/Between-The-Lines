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

@app.route("/song/<song_id>")
def song(song_id):
    # Dummy song info for now
    song_info = {
        "id": song_id,
        "name": "Dummy Song Name",
        "artists": ["Dummy Artist 1", "Dummy Artist 2"],
        "album_name": "Dummy Album",
        "release_date": "2024-01-01",
        "popularity": 87,
        "cover_url": "https://via.placeholder.com/400x400?text=Album+Cover",
        "preview_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"  # example mp3
    }

    # Dummy recommendations (for playlist player)
    recommendations = [
        {
            "id": "rec1",
            "name": "Recommended Song 1",
            "artist": "Artist 1",
            "preview_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
            "cover_url": "https://via.placeholder.com/200x200?text=Rec+1"
        },
        {
            "id": "rec2",
            "name": "Recommended Song 2",
            "artist": "Artist 2",
            "preview_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
            "cover_url": "https://via.placeholder.com/200x200?text=Rec+2"
        },
        {
            "id": "rec3",
            "name": "Recommended Song 3",
            "artist": "Artist 3",
            "preview_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
            "cover_url": "https://via.placeholder.com/200x200?text=Rec+3"
        },
    ]

    return render_template("song.html", song=song_info, recommendations=recommendations)


if __name__ == "__main__":
    app.run(debug=True)
