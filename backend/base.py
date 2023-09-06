from flask import Flask
from flask import request
import sys
sys.path.append('./app')
from app.main import getRecommendations, refresh, getChartData

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
    

@api.route('/visualize')
def visualize():
    print("Getting chart data")
    query_playlist = request.args.get('playlist')
    query_key = request.args.get('key')
    playlist_id = query_playlist.split('/')[-1]
    print(query_key)

    chartData = getChartData(playlist_id, query_key)
    print("Returning chart data")
    return chartData

# if __name__ == '__main__':
#     api.run(host="localhost", port=3000, debug=False)