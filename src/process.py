# process data about tracks and playlists
import requests
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas


# processes track data and audio data into dictionary
def processTrack(headers, track_content, run = True):
    if not run: return
    # try: # this method was far too slow and typically timed out - too many requests
    #     track_res = requests.get(f'https://api.spotify.com/v1/tracks/{id}', headers=headers)
    #     track_content = track_res.json()
    #     audio_res = requests.get(f'https://api.spotify.com/v1/audio-analysis/{id}', headers=headers)
    #     audio_content = audio_res.json()
    # except TimeoutError:
    #     return ['timeout', 0, 0, 0, 0, 0, 0, 0, 0]

    track_frame = []
    # album info should be scored lower than track and audio information
    print(track_content['track'].keys())
    track_frame.append(track_content['track']['name'])
    track_frame.append(track_content['track']['album']['name'])
    track_frame.append(track_content['track']['album']['release_date'])
    track_frame.append(track_content['track']['artists'][0]['id'])
    track_frame.append(track_content['track']['popularity'])
    
    # track_frame.append(track_content['track']['duration'])
    # track_frame.append(track_content['track']['loudness'])
    # track_frame.append(track_content['track']['tempo']) #possibly use tempo confidence to weight
    # track_frame.append(track_content['track']['key'])
    # track_frame.append(track_content['track']['mode'])
    return track_frame

def processPlaylist(headers, res, run = True):
    if not run: return
    
    playlist = res.json()['tracks']['items']
    playlist_frame = {
        'name' : [],
        'album' : [],
        'release' : [],
        'artist' : [],
        'popularity' : [],
        # 'duration' : [],
        # 'loudness' : [],
        # 'tempo'  : [],
        # 'key' : [],
        # 'mode' : []
        }
    playlist_frame = pandas.DataFrame(playlist_frame)
    
    for i,song in enumerate(playlist):
        playlist_frame.loc[i] = processTrack(headers, song)
            
    playlist_frame.to_csv('./txt/dataframe.csv')