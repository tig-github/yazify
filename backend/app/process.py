# process data about tracks and playlists
import requests
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas
from time import sleep

# processes track data and audio data into dictionary
def processTrack(track_content, audio_content, run = True):

    if not run: return
    track_frame = [
        track_content['name'],
        track_content['album']['name'],
        track_content['album']['release_date'],
        track_content['artists'][0]['id'],
        track_content['popularity'],
        audio_content['acousticness'],
        audio_content['danceability'],
        audio_content['duration_ms'],
        audio_content['energy'],
        audio_content['instrumentalness'],
        audio_content['liveness'],
        audio_content['loudness'],
        audio_content['mode'],
        audio_content['tempo'],
        audio_content['valence']
    ]
    # album info should be scored lower than track and audio information
    return track_frame


# takes batch of 100 tracks and processes data onto csv
def processTrackBatch(headers, playlist_frame, ids, run = True):
    if not run: return
    #ids = str(ids).lstrip('[').rstrip(']')
    #ids = ','.join(ids)
    notNone = lambda x : x != None
    
    ids1 = ','.join(list(filter(notNone, ids))[:50])
    ids2 = ','.join(list(filter(notNone, ids))[50:])

    track_batch1 = requests.get(f'https://api.spotify.com/v1/tracks?ids={ids1}', headers=headers)
    audio_batch1 = requests.get(f'https://api.spotify.com/v1/audio-features?ids={ids1}', headers=headers)
    prev_length = len(playlist_frame)
    for i in range(min(len(audio_batch1.json()['audio_features']), len(track_batch1.json()['tracks']))):
        if not audio_batch1.json()['audio_features'][i]:
            continue
        processed_tracks1 = processTrack(track_batch1.json()['tracks'][i], audio_batch1.json()['audio_features'][i])
        playlist_frame.loc[i+prev_length] = processed_tracks1

    if not ids2: return
    track_batch2 = requests.get(f'https://api.spotify.com/v1/tracks?ids={ids2}', headers=headers)
    audio_batch2 = requests.get(f'https://api.spotify.com/v1/audio-features?ids={ids1}', headers=headers)

    prev_length = len(playlist_frame)
    for i in range(min(len(audio_batch2.json()['audio_features']), len(track_batch2.json()['tracks']))):
        if not (audio_batch2.json()['audio_features'][i] and track_batch2.json()['tracks'][i]):
            continue
        #print('index error at i=',i,'for batch of lengths', len(audio_batch2.json()['audio_features']), len(track_batch2.json()['tracks']))
        processed_tracks2 = processTrack(track_batch2.json()['tracks'][i], audio_batch2.json()['audio_features'][i])
        playlist_frame.loc[i+prev_length] = processed_tracks2

    #sleep(2) # to avoid rate limiting
    return playlist_frame


#user will refer to a single user-inputted track
def processUser(headers, id, run = True):
    if not run: return
    
    user_frame = {
        'name' : [],
        'album' : [],
        'release' : [],
        'artist' : [],
        'popularity' : [],
        'acousticness' : [],
        'danceability' : [],
        'duration' : [],
        'energy' : [],
        'insturmentalness' : [],
        'liveness' : [],
        'loudness' : [],
        'mode' : [],
        'tempo' : [],
        'valence' : []
        }
    user_frame = pandas.DataFrame(user_frame)
    
    track_content = requests.get(f'https://api.spotify.com/v1/tracks/{id}', headers=headers)
    audio_content = requests.get(f'https://api.spotify.com/v1/audio-features/{id}', headers=headers)

    user_frame.loc[0] = processTrack(track_content.json(), audio_content.json(), run = True)
    user_frame.to_csv('./app/csv/user.csv')    


# processes playlist data into csv
def processPlaylist(headers, res, run = True):
    if not run: return

    playlist = res.json()['tracks']
    playlist_frame = {
        'name' : [],
        'album' : [],
        'release' : [],
        'artist' : [],
        'popularity' : [],
        'acousticness' : [],
        'danceability' : [],
        'duration' : [],
        'energy' : [],
        'insturmentalness' : [],
        'liveness' : [],
        'loudness' : [],
        'mode' : [],
        'tempo' : [],
        'valence' : []
        }
    playlist_frame = pandas.DataFrame(playlist_frame)
    while playlist:
        ids = [track['track']['id'] for track in playlist['items']]
        playlist_frame = processTrackBatch(headers, playlist_frame, ids)
        try:
            playlist = requests.get(playlist['next'], headers=headers).json()
        except requests.exceptions.MissingSchema:
            break #finished scraping playlist
    playlist_frame.to_csv('./app/csv/dataframe.csv')