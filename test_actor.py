import requests
import json
import pprint

page_num1 = 1
movie_lst1 = []

while page_num1 <= 499:
  URL = f'https://api.themoviedb.org/3/movie/popular?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR&page={page_num1}'
  response1 = requests.get(URL).json()
  results1 = response1['results']
  for result in results1:
    if result['vote_count'] < 100:
      continue
    else:
      movie_lst1.append(result)
  page_num1 += 1

# pprint.pprint(movie_lst)
# print(len(movie_lst[0]))

popular_movies = []

for movie in movie_lst1:
    try:
        ACTORS_URL = f'https://api.themoviedb.org/3/movie/{int(movie["id"])}/credits?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR'
        response2 = requests.get(ACTORS_URL).json()
        # popular_movies_actors.append(response1["cast"])

        # popular_movies_actors1 배열에 {'actor_pk' : int(id) }가 여러개 들어갔다고 
        cnt1 = 0
        actor_lst = []
        for cast1 in response2["cast"]:
          if cnt1 == 5:
            break
          if cast1["known_for_department"] != "Acting":
            continue
          else:
              if cast1["id"] not in actor_lst:
                actor_lst.append(cast1["id"])
              else:
                continue
              cnt1 += 1

        movies_dict = dict()
        movies_dict["model"] = 'movies.movie'
        # print(movie)
        fields_dict = dict()
        fields_dict['title'] = movie["title"]
        fields_dict['tmdb_id'] = movie["id"]

        fields_dict['release_date'] = movie["release_date"]
        fields_dict['popularity'] = movie["popularity"]
        fields_dict['vote_count'] = movie["vote_count"]
        fields_dict['vote_average'] = movie["vote_average"]
        fields_dict['overview'] = movie["overview"]
        fields_dict['poster_path'] = movie["poster_path"]
        fields_dict['genres'] = movie["genre_ids"]
        
        fields_dict['actors'] = actor_lst

        fields_dict['like_users'] = []
        movies_dict['fields'] = fields_dict
        popular_movies.append(movies_dict)
        pprint.pprint(movies_dict)
        print()

    except KeyError:
        movies_dict = dict()
        continue
    except UnicodeEncodeError:
        movies_dict = dict()
        continue
    except FileNotFoundError:
        movies_dict = dict()
        continue
    except KeyboardInterrupt:
        movies_dict = dict()
        continue

print(len(popular_movies))

#######################################################

# page_num = 1
# movie_lst = []

# while page_num <= 499:
#     URL = f'https://api.themoviedb.org/3/movie/popular?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR&page={page_num}'
#     response = requests.get(URL).json()
#     movie_lst.append(response['results'])
#     page_num += 1

# popular_movies = []
# popular_movies_actors = []

# for i in range(len(movie_lst)-1):
#     for movie in movie_lst[i]:
#         try:
#             ACTORS_URL = f'https://api.themoviedb.org/3/movie/{movie["id"]}/credits?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR'
#             response3 = requests.get(ACTORS_URL).json()
#             casts = response3["cast"]
                

        # except KeyError:
        #     movies_dict = dict()
        #     continue
        # except UnicodeEncodeError:
        #     movies_dict = dict()
        #     continue
        # except FileNotFoundError:
        #     movies_dict = dict()
        #     continue
        # except KeyboardInterrupt:
        #     movies_dict = dict()
        #     continue

with open("./popular_actors.json", 'w', encoding='UTF-8') as f:
  json.dump(popular_movies, f, indent=4, ensure_ascii=False)

pprint.pprint(popular_movies)