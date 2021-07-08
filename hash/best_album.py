from collections import defaultdict

def solution(genres, plays):
    answer = []
    dic_cnt_genres = {}
    dic_genres_plays = defaultdict(lambda: [])
    
    for i in range (len(genres)):
        if genres[i] not in dic_cnt_genres:
            dic_cnt_genres[genres[i]] = plays[i]
        else:
            dic_cnt_genres[genres[i]] += plays[i]
        dic_genres_plays[genres[i]].append((plays[i],i))

    dic_cnt_genres = dict(sorted(dic_cnt_genres.items(), key=lambda x : x[1], reverse=True))

    for i in dic_genres_plays:
        play_sort = sorted(dic_genres_plays.get(i), key=lambda x : x[0], reverse=True)
        dic_genres_plays[i] = []

        if len(play_sort) > 1:
            dic_genres_plays[i].append(play_sort[0][1])
            dic_genres_plays[i].append(play_sort[1][1])
        else:
            dic_genres_plays[i].append(play_sort[0][1])

    for i in dic_cnt_genres.keys():
        if len(dic_genres_plays.get(i)) > 1:
            answer.extend(dic_genres_plays.get(i))
        else:
            answer.append(dic_genres_plays.get(i)[0])
    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))