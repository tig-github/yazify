import requests
import json
from secret import client_id, client_secret
from scrape import scrapePlaylist


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
    # id = 'anytrackuri' #testing on any track
    # res =requests.get(f'https://api.spotify.com/v1/tracks/{id}', headers=headers)
    # content = res.json()
    # with open('content.txt', 'w') as f:
    #     for category in content.keys():
    #         f.write(f'{category}:\n')
    #         try:
    #             iter(content)
    #             for line in content[category]:
    #                 f.write(f'{line}\n')
    #             f.write('\n')
    #         except TypeError:
    #             continue
    scrapePlaylist(headers)