import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("CLID"),
    client_secret=os.getenv("SECRET")
))

def search_song(song_name: str) -> dict:
    results = sp.search(q=song_name, limit=1)
    return results["tracks"]["items"][0] if results["tracks"]["items"] else None

# TESTING: Call the function and print result
if __name__ == "__main__":
    song_name = "DtMF"  # Contoh lagu
    song_data = search_song(song_name)
    
    if song_data:
        print(f"Song Name: {song_data['name']}")
        print(f"Artist: {', '.join(artist['name'] for artist in song_data['artists'])}")
        print(f"Album: {song_data['album']['name']}")
        print(f"Spotify URL: {song_data['external_urls']['spotify']}")
    else:
        print("Song not found.")