import requests
import json

def scrapePlaylist(headers, run = True):
    if not run: return
    id = '2ttf8zNG34K5SSdZRzqhVR?si=574666c4176c41d0' #playlist will scrape for now - can expand later
    res = requests.get(f'https://api.spotify.com/v1/playlists/{id}', headers=headers)
    next_res = res.json()['tracks']
    song_num = 0
    content = next_res
    while next_res:
        with open('./txt/playlist.txt', 'a', encoding="utf-8") as f:
            for track in content['items']:
                f.write(f"{song_num} : {track['track']['name']}\n")
                song_num += 1
        next_res = content['next']
        try:
            next_res = requests.get(next_res, headers=headers)
        except requests.exceptions.MissingSchema:
            break #finished scraping playlist
        content = next_res.json()


