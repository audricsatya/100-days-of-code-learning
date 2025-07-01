# Library List
from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

date_input = input("Which year do you want to travel to? (Format: YYYY-MM-DD): ")

SPOTIPY_CLIENT_ID = os.environ.get("")
SPOTIPY_CLIENT_SECRET = os.environ.get("")
SPOTIPY_REDIRECT_URI = os.environ.get("")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_input}", headers=header)
resp_text = response.text
soup = BeautifulSoup(resp_text, features='html.parser')
song_list = soup.select("li ul li h3")
singer_list = soup.select("span.c-label.a-no-trucate")
song_title = [song.getText().strip() for song in song_list]
song_singer = [singer.getText().strip() for singer in singer_list]

spotifyClientId = os.environ["SPOTIFY_CLIENT_ID"]
spotifyClientSecret=os.environ["SPOTIFY_CLIENT_SECRET"]
spotifyRedirectURI=os.environ["SPOTIFY_REDIRECT_URI"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotifyClientId ,
    client_secret=spotifyClientSecret,
    redirect_uri=spotifyRedirectURI,
    show_dialog=True,
    cache_path="token.txt",
    username="boomerbob",
    scope="playlist-modify-private")
)

print(f"SP: {sp}")
user_id = sp.current_user()["id"]
print(f"SP User: {user_id}")

song_uris = []
year = date_input.split("-")[0]
for song in song_title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)