import requests
import os
from secret import client_id, client_secret
from scrape import scrapePlaylist
from score import scoreSimilarity, getScores, testScores
from explore import *
from process import *



def setup():
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
    return headers


# called by frontend given song to return all recommendations
def getRecommendations(song_id):
    headers = setup()
    processUser(headers, id = song_id, run = True)
    scoreSimilarity('./app/csv/user.csv', './app/csv/dataframe.csv', metric = "cosine", run = True)
    scores = getScores(headers, './app/csv/scores.csv', run = True)
    return scores


# refreshes the representative playlist for updates
def refresh():
    headers = setup()
    playlist_response = scrapePlaylist(headers, run = True, save = True)
    processPlaylist(headers, playlist_response, run = True)

# for exploring track data
def explore():
    #headers = setup()
    #playlist_response = scrapePlaylist(headers, run = True, save = False)
    #processPlaylist(headers, playlist_response, run = True)
    releases = processReleases('./app/csv/dataframe.csv')
    plotReleases(releases)


if __name__ == '__main__':
    explore()
    #testScores('./csv/user.csv', './csv/dataframe.csv')
    # scoreSimilarity('./csv/user.csv', './csv/dataframe.csv', run = True)
    # getScores('./csv/scores.csv', run = True)
    # playlist_response = scrapePlaylist(headers, run = False, save = False)
    # exploreTracks(headers, id = '4FyesJzVpA39hbYvcseO2d?si=6007e7e8fd4e4b89', run = False)
    # exploreAudio(headers, id = '4FyesJzVpA39hbYvcseO2d?si=6007e7e8fd4e4b89', run = False)
    # explorePlaylist(headers, id= '2ttf8zNG34K5SSdZRzqhVR?si=574666c4176c41d0', run = False)
    # processPlaylist(headers, playlist_response, run = False)
    # processUser(headers, id = '1DZx0LEctNXUHQ9VQFKlgl?si=6508fbe3086b415a', run = True)
    # scoreSimilarity('./csv/user.csv', './csv/dataframe.csv', run = True)
    # getScores('./csv/scores.csv', run = True)