# simple utility functions
import requests
import json


# get artist name from id
def getArtist(headers, id):
    res = requests.get(f'https://api.spotify.com/v1/artists/{id}', headers=headers)
    res = res.json()
    print('!!!!!!!!!!!!!!!!1', res)
    if 'name' not in res:
        return id 
    else:
        return res['name']
