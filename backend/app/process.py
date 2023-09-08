# process data about tracks and playlists
import requests
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas
from time import sleep
from utils import getArtist

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
    print(track_batch1, audio_batch1)
    prev_length = len(playlist_frame)
    for i in range(min(len(audio_batch1.json()['audio_features']), len(track_batch1.json()['tracks']))):
        if not audio_batch1.json()['audio_features'][i]:
            continue
        processed_tracks1 = processTrack(track_batch1.json()['tracks'][i], audio_batch1.json()['audio_features'][i])
        print(processed_tracks1)
        playlist_frame.loc[i+prev_length] = processed_tracks1

    if not ids2: return playlist_frame
    track_batch2 = requests.get(f'https://api.spotify.com/v1/tracks?ids={ids2}', headers=headers)
    audio_batch2 = requests.get(f'https://api.spotify.com/v1/audio-features?ids={ids1}', headers=headers)
    print(track_batch2, audio_batch2)

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
def processPlaylist(headers, res, save = True, run = True):
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
        #print(playlist_frame)
        #sleep(30)
        try:
            playlist = requests.get(playlist['next'], headers=headers).json()
        except requests.exceptions.MissingSchema:
            break #finished scraping playlist
    if save: playlist_frame.to_csv('./app/csv/dataframe.csv')
    return playlist_frame
    
    
# same as processPlaylist, but will continually expand the df instead of replaciging it
def processPlaylistAddition(headers, res, run = True):
    if not run: return
    
    playlist_frame = pandas.read_csv('./app/csv/dataframe.csv')
    if len(playlist_frame.index) == 0:
        playlist_frame = processPlaylist(headers, res)
    else: #have to remove first column for it to work
        playlist_frame = playlist_frame.iloc[: , 1:]
    #continue_index = len(playlist_frame.index)
    
    playlist = res.json()['tracks']
    while playlist:
        ids = [track['track']['id'] for track in playlist['items']]
        playlist_frame = processTrackBatch(headers, playlist_frame, ids)
        try:
            playlist = requests.get(playlist['next'], headers=headers).json()
        except requests.exceptions.MissingSchema:
            break #finished scraping playlist
    playlist_frame.to_csv('./app/csv/dataframe.csv')
    
    
# gather how many songs were released each year
# takes in dataframe
def processReleases(playlist_df):
    #playlist_df = pandas.read_csv(playlist_df)
    releases = {}
    for song in playlist_df['release']:
        year = song[:4]
        if year in releases:
            releases[year] += 1
        else:
            releases[year] = 1
    return sorted([{'name':k, 'value':v} for k,v in releases.items()], key=lambda x:x['name'])
    
    
# gathers all artists and how many songs they have in the playlist
def processArtists(headers, playlist_df):
    releases = {}
    for artist in playlist_df['artist']:
        if artist in releases:
            releases[artist] += 1
        else:
            releases[artist] = 1

    return [{'name':getArtist(headers, k), 'value':v} for k,v in releases.items()]


# gathers all albums and how many songs they have in the playlist
def processAlbums(playlist_df):
    releases = {}
    for album in playlist_df['album']:
        if album in releases:
            releases[album] += 1
        else:
            releases[album] = 1
    return [{'name':k, 'value':v} for k,v in releases.items()]