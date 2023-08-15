import pandas
import numpy as np
import math

# brute force approach to scoring
# simply calculate similarity weighting different features differently
def bruteForce(user, playlist):
    bool_similarity = lambda user,song,w : (user == song) * w 
    cont_similarity = lambda user,song,w,c : c*abs(user - song) * w
    multisum = lambda *args : sum(args)
    #multiprint = lambda *args : print(args)
    
    user = pandas.read_csv(user)
    playlist = pandas.read_csv(playlist)
    scores = {
        'name' : [],
        'score' : []
    }
    scores_frame = pandas.DataFrame(scores)
    
    for i in range(len(playlist)):
        name_score = bool_similarity(user['name'][0], playlist.loc[i]['name'], .01) # name can have 0-weight too
        album_score = bool_similarity(user['album'][0], playlist.loc[i]['album'], .1) # name can have 0-weight too
        # release_score = _
        artist_score = bool_similarity(user['artist'][0], playlist.loc[i]['artist'], .1)
        popularity_score = cont_similarity(user['popularity'][0], playlist.loc[i]['popularity'], 1, .01)
        acoustic_score = cont_similarity(user['acousticness'][0], playlist.loc[i]['acousticness'], 1.5, 1)
        danceability_score = cont_similarity(user['danceability'][0], playlist.loc[i]['danceability'], 1, 1)
        duration_score = cont_similarity(user['duration'][0], playlist.loc[i]['duration'], .5, .000001)
        energy_score = cont_similarity(user['energy'][0], playlist.loc[i]['energy'], 1.5, 1)
        insturmentalness_score = cont_similarity(user['insturmentalness'][0], playlist.loc[i]['insturmentalness'], 1, .01)
        liveness_score = cont_similarity(user['liveness'][0], playlist.loc[i]['liveness'], 1, 1)
        loudness_score = cont_similarity(user['loudness'][0], playlist.loc[i]['loudness'], 1, .01)
        mode_score = bool_similarity(user['artist'][0], playlist.loc[i]['artist'], 1.5)
        tempo_score = cont_similarity(user['tempo'][0], playlist.loc[i]['tempo'], .75, .001)
        valence_score = cont_similarity(user['valence'][0], playlist.loc[i]['valence'], 3, 1)
        
        # multiprint(name_score, album_score, artist_score, popularity_score, acoustic_score, danceability_score,
        #                                       duration_score, energy_score, insturmentalness_score, liveness_score, loudness_score,
        #                                       mode_score, tempo_score, valence_score)
        
        scores_frame.loc[i] = [playlist.loc[i]['name'],
                multisum(name_score, album_score, artist_score, popularity_score, acoustic_score, danceability_score,
                                                duration_score, energy_score, insturmentalness_score, liveness_score, loudness_score,
                                                mode_score, tempo_score, valence_score)]
    return scores_frame

# more effective scoring using geometric similarity - testing has proven this very ineffective
def cosineSimilarity(user, playlist):
    magnitude = lambda x : math.sqrt(np.sum(np.power(x, 2)))
    cos_similarity = lambda x,y : np.dot(x,y) / (magnitude(x) * magnitude(y))
    user = pandas.read_csv(user).to_numpy()
    playlist_df = pandas.read_csv(playlist) # save separately to build scores df after calculating cosine score
    playlist = playlist_df.to_numpy()
    scores = {
        'name' : [],
        'score' : []
    }
    scores_frame = pandas.DataFrame(scores)
    playlist = np.delete(playlist, (0), axis=0)
    for _ in range(5):
        user = np.delete(user, 0, axis=1)
        playlist = np.delete(playlist, 0, axis=1)
    user.reshape(-1)
    # create scores by comparing each vector with cosine similarity metric
    for i in range(len(playlist)):
        similarity = cos_similarity(user, playlist[i]).T
        scores_frame.loc[i] = [playlist_df.loc[i]['name'], similarity[0]]
    return scores_frame
    

def scoreSimilarity(user, playlist, metric="cosine", run = True):
    if not run: return
    if metric == "brute":
        scores_frame = bruteForce(user, playlist)
    elif metric == "cosine":
        scores_frame = cosineSimilarity(user, playlist)
    scores_frame.to_csv('./app/csv/scores.csv')

# returns highest 5 scores
def getScores(scores, run = True):
    if not run: return
    print('res')
    scores = pandas.read_csv(scores)
    scores = scores.sort_values(by = 'score', ascending = False)
    scores.drop(columns = scores.columns[0], axis = 1, inplace= True)
    scores.to_csv('./app/csv/sorted.csv')
    print(scores)
    res = scores['name'].values.tolist()[:5]
    print(res)
    return res


def testScores(user, playlist):
    scores_frame = cosineSimilarity(user, playlist)
    scores_frame.to_csv('./csv/testScores.csv')