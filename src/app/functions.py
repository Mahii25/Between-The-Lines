import requests
import base64
import os
from flask import session
from app.config_secrets import APP_SECRET, APP_ID

REDIRECT_URI = "http://127.0.0.1:5000/logging_in"

# Step 1: generate Spotify auth URL
def get_auth_url():
    scopes = "user-top-read"
    url = (
        f"https://accounts.spotify.com/authorize?client_id={APP_ID}"
        f"&response_type=code&redirect_uri={REDIRECT_URI}&scope={scopes}"
    )
    return url

# Step 2: exchange code for access token
def get_token(code):
    auth_str = f"{APP_ID}:{APP_SECRET}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {b64_auth_str}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }

    response = requests.post(token_url, data=data, headers=headers)
    return response.json()

def get_song_info(access_token, song_id):
    url = f"https://api.spotify.com/v1/tracks/{song_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

