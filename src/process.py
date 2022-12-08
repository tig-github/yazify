# process data about tracks and playlists
import requests
import pandas


# processes track data and audio data into pandas df
def processTrack(headers, id, run = False):
    if not run: return
    track_res = requests.get(f'https://api.spotify.com/v1/tracks/{id}', headers=headers)
    track_content = track_res.json()
    audio_res = requests.get(f'https://api.spotify.com/v1/audio-analysis/{id}', headers=headers)
    audio_content = audio_res.json()
    
    track_frame = {}
    
    # album info should be scored lower than track and audio information
    track_frame['album'] = track_content['album']['name']
    track_frame['date'] = track_content['album']['release_date']
    track_frame['artists'] = track_content['artists'][0]['id']
    track_frame['popularity'] = track_content['popularity']
    
    track_frame['duration'] = audio_content['track']['duration']
    track_frame['loudness'] = audio_content['track']['loudness']
    track_frame['tempo'] = audio_content['track']['tempo'] #possibly use tempo confidence to weight
    track_frame['key'] = audio_content['track']['key']
    track_frame['mode'] = audio_content['track']['mode']
        
    track_frame = pandas.DataFrame(track_frame, index=[0])
    print(track_frame)
    

# the idea is to process some user information to generate scores for each track
def processUser():
    pass