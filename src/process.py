# process data about tracks and playlists
import requests
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas


# processes track data and audio data into dictionary
def processTrack(track_content, audio_features_content, run = True):
    if not run: return

    track_frame = [
        track_content['track']['name'],
        track_content['track']['album']['name'],
        track_content['track']['album']['release_date'],
        track_content['track']['artists'][0]['id'],
        track_content['track']['popularity'],
    ]
    # album info should be scored lower than track and audio information
    
    return track_frame


# takes batch of 100 tracks and processes data onto csv
def processTrackBatch(headers, playlist_frame, ids, run = True):
    if not run: return
    #ids = str(ids).lstrip('[').rstrip(']')
    ids = ','.join(ids)
    track_batch = requests.get(f'https://api.spotify.com/v1/track-features/{str(ids)}', headers=headers)
    audio_batch = requests.get(f'https://api.spotify.com/v1/audio-features/{str(ids)}', headers=headers)
    print(track_batch.json())
    # for i,x in enumerate(track_batch): #pseudocode
    #     playlist_frame.loc[i] = processTrack(track_batch.json(), audio_batch.json())
    # return playlist_frame


def processPlaylist(headers, res, run = True):
    if not run: return

    playlist = res.json()
    playlist_frame = {
        'name' : [],
        'album' : [],
        'release' : [],
        'artist' : [],
        'popularity' : [],
        }
    playlist_frame = pandas.DataFrame(playlist_frame)
    while playlist:
        ids = [track['track']['id'] for track in playlist['tracks']['items']]
        playlist_frame = processTrackBatch(headers, playlist_frame, ids)
        try:
            playlist = requests.get(playlist['next'], headers=headers)
        except requests.exceptions.MissingSchema:
            break #finished scraping playlist
    playlist_frame.to_csv('./txt/dataframe.csv')