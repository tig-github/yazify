# test file just to explore structure of json objects returned by spotify api
import requests
import pandas


# explores general information from a track
def exploreTracks(headers, id = '', run = True):
    if not run: return
    res = requests.get(f'https://api.spotify.com/v1/tracks/{id}', headers=headers)
    content = res.json()
    with open('./txt/content.txt', 'w') as f:
        for category in content.keys():
            f.write(f'{category}:\n')
            try:
                iter(content[category])
                if type(content[category]) == str:
                    print(content[category])
                    continue
                for line in content[category]:
                    f.write(f'{line}\n')
                f.write('\n')
            except TypeError:
                continue
            
# explores audio data of a track
def exploreAudio(headers, id = '', run = True):
    if not run: return
    res = requests.get(f'https://api.spotify.com/v1/audio-analysis/{id}', headers=headers)
    content = res.json()
    with open('./txt/audio.txt', 'w') as f:
        for category in content.keys():
            f.write(f'{category}:\n')
            try:
                iter(content[category])
                if type(content[category]) == str:
                    print(content[category])
                    continue
                for line in content[category]:
                    f.write(f'{line}\n')
                f.write('\n')
            except TypeError:
                continue
           
def explorePlaylist(headers, id = '', run = True):
    if not run: return
    res = requests.get(f'https://api.spotify.com/v1/playlists/{id}', headers=headers)
    content = res.json()
    with open('./txt/playlistcontent.txt', 'w') as f:
        for category in content.keys():
            f.write(f'{category}:\n')
            try:
                iter(content[category])
                if type(content[category]) == str:
                    print(content[category])
                    continue
                for line in content[category]:
                    f.write(f'{line}\n')
                f.write('\n')
            except TypeError:
                continue