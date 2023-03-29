from flask import Flask
from flask import request
import sys
sys.path.append('./app')
from app.main import getRecommendations

api = Flask(__name__)

@api.route('/songs')
def my_songs():
    print('Getting song scores')
    song_id = request.args.get('song')
    songs = getRecommendations(song_id)
    response_body = {
        "songs": songs,
    }
    print('Returning song scores')

    return response_body

# if __name__ == '__main__':
#     api.run(host="localhost", port=3000, debug=False)