import requests
import json
from secret import client_id, client_secret
from scrape import scrapePlaylist
from explore import *
from process import *


auth_url = 'https://accounts.spotify.com/api/token'

auth_options = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
})

auth_data = auth_options.json()
access_token = auth_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# 'https://api.spotify.com/v1/audio-analysis/id' for analyzing audio features
# 'https://api.spotify.com/v1/tracks/id' for analyzing track features

if __name__ == '__main__':
    playlist_response = scrapePlaylist(headers, run = True, save = False)
    exploreTracks(headers, id = '4FyesJzVpA39hbYvcseO2d?si=6007e7e8fd4e4b89', run = False)
    exploreAudio(headers, id = '4FyesJzVpA39hbYvcseO2d?si=6007e7e8fd4e4b89', run = False)
    explorePlaylist(headers, id= '2ttf8zNG34K5SSdZRzqhVR?si=574666c4176c41d0', run = False)
    processPlaylist(headers, playlist_response, run = True)