import requests
import json
import os

def scrapePlaylist(headers, id = '2ttf8zNG34K5SSdZRzqhVR?si=574666c4176c41d0', run = True, save = True):
    if not run: return
    if save: open('./app/txt/playlist.txt', 'w').close()
    if save: open('./app/txt/index.json', 'w').close()
    res = requests.get(f'https://api.spotify.com/v1/playlists/{id}', headers=headers)
    next_res = res.json()['tracks']
    song_num = 0
    content = next_res
    index = {} # initialize each track score to 0, for now will save index in-memory 
    while next_res:
        #print(os.path.isfile('./app/txt/playlist.txt'))
        with open('./app/txt/playlist.txt', 'a', encoding="utf-8") as f:
            for track in content['items']:
                if save: f.write(f"{song_num} : {track['track']['name']}\n")
                song_num += 1
                index[track['track']['id']] = track['track']['name']
        next_res = content['next']
        try:
            next_res = requests.get(next_res, headers=headers)
        except requests.exceptions.MissingSchema:
            break #finished scraping playlist
        content = next_res.json()
    with open("./app/txt/index.json", "w") as f:
        if save: json.dump(index, f)
    return res

