from flask import Flask
from flask import request
import sys
sys.path.append('./app')
from app.main import getRecommendations, refresh

api = Flask(__name__)

@api.route('/songs')
def my_songs():
    print('Getting song scores')
    query_song = request.args.get('song')
    song_id = query_song.split('/')[-1]
    songs = getRecommendations(song_id)
    response_body = {
        "songs": songs,
    }
    print('Returning song scores')
    return response_body

@api.route('/refresh')
def refresh_songs():
    print('Updating song database')
    refresh()
    print('Finished updating the song database')
    

# if __name__ == '__main__':
#     api.run(host="localhost", port=3000, debug=False)