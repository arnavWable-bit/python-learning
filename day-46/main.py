from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import requests
from pprint import pprint

date =  input("Which year would you like to travel to? Type the date in YYYY-MM-DD format: ")

URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
headers = {
   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
bakeboard_webpage = response.text

soup = BeautifulSoup(bakeboard_webpage, "html.parser")

songs = soup.find_all(name='h3', class_= 'chart-entry__title')

song_titles = [song.getText(strip=True) for song in songs]

yt = YTMusic("day-46/browser.json")
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

playlist_title = f'{date} Billboard Top 100'

params = {
    'title' : playlist_title,
    'description' : f"Time travel playlist for {date}"
}

playlist_exists = False

for playlist in playlists:
    if playlist["title"] == playlist_title:
        playlist_exists = True
        playlist_id = playlist["playlistId"]
        break

if not playlist_exists:
    playlist_id = yt.create_playlist(**params)
    print("Playlist created!")
else:
    print("Playlist already exists.")
    
    
song_ids = []

for song in song_titles:
    try:
        results = yt.search(query=song, filter='songs')
        song_ids.append(results[0]['videoId'])
    except:
        print(f"{song} doesn't exist in YouTube Music. Skipped.")

yt.add_playlist_items(playlistId=playlist_id, videoIds=song_ids)