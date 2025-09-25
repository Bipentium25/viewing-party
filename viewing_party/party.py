# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    # those three attributes are truthy
    if not (title and genre and rating):
        return None
    
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    
    return movie

def add_to_watched(user_data, movie):
    # empty list is a valid value
    # user_data = {"watched": [{},{},{}]}

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    # user_data = {"watchlist": [{},{},{}]}

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    # should we add a test to reply the movie which is
    # not in watchlist that watched by user? like adding
    # to the watched list?

    for index_dic in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][index_dic]["title"]:
            user_data["watched"].append(user_data["watchlist"][index_dic])
            user_data["watchlist"].pop(index_dic)

    return user_data
    





# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_rating = 0
    average_rating = 0
    if not user_data["watched"]:
        return average_rating
    for i in range(len(user_data["watched"])):
        total_rating += user_data["watched"][i]["rating"]
    average_rating = total_rating/len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    genere_dict = {}

    if not user_data["watched"]:
        return None
    for i in range(len(user_data["watched"])):
        genere_dict[user_data["watched"][i]["genre"]] = genere_dict.get(user_data["watched"][i]["genre"],0) + 1
    
    max_genere = ["genere", -1000]

    for genere_key, genere_value in genere_dict.items():
        if genere_value > max_genere[1]:
            max_genere = [genere_key, genere_value]

    return max_genere[0]
    # genre_count = 0
    # most_popular_genre = " "
    # for genere_key, genere_value in genere_dict.items():
    #     if genere_value > genre_count:
    #         most_popular_genre = genere_key
    #         genre_count = genere_value

    # return most_popular_genre


# # USER_DATA_2b = {
#     "watched": [
#         INTRIGUE_1,
#         FANTASY_2,
#         ACTION_1,
#         {
#     "title": "The Lord of the Functions: The Fellowship of the Function",
#     "genre": "Fantasy",
#     "rating": 4.8
# },
#         FANTASY_3,
#         INTRIGUE_2,
#     ],
#     "friends": [
#         {
#             "watched": [
#                 { "title": "The Lord of the Functions: The Fellowship of the Function",
#                      "genre": "Fantasy",
#                         "rating": 4.8, 
#                           "host" = "netflix"},
#                 FANTASY_3,
#                 FANTASY_4,
#                 HORROR_1,
#             ]
#         },
#         {
#             "watched": [
#                 FANTASY_1,
#                 ACTION_1,
#                 INTRIGUE_1,
#                 INTRIGUE_3,
#             ]
#         }
#     ]  
# }

# def get_unique_watched(user_data):
#     unique_watched = []
#     duplicate = False
#     for i in range(len(user_data["watched"])):
#         duplicate = False
#         # if item is in set(t1, t2, t3):
#         for n in range(len(user_data["friends"])):
#             for m in range(len(user_data["friends"][n]["watched"])):
#                 if user_data["watched"][i]["title"] == user_data["friends"][n]["watched"][m]["title"]:
#                     duplicate = True
#                     break
#             if duplicate:
#                 break
#         if not duplicate: 
#             unique_watched.append(user_data["watched"][i])

#     # if  user_data["watched"][i]["title"] != user_data["friends"][n]["watched"][m]["title"]:    
#     return   unique_watched
def get_title_friends_watched(user_data):
    movie_titile_friends_watched = set()

    for d in user_data["friends"]:
        for d_movie in d["watched"]:
            movie_titile_friends_watched.add(d_movie["title"])

    return movie_titile_friends_watched

def get_unique_watched(user_data):
    unique_watched = []

    for movie in (user_data["watched"]):
        if movie["title"] not in get_title_friends_watched(user_data):
            unique_watched.append(movie)

    return   unique_watched

def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    set_movie_title = get_title_friends_watched(user_data)

    for movie in (user_data["watched"]):
        if movie["title"] in set_movie_title:
            set_movie_title.remove(movie["title"])

    for d in user_data["friends"]:
        for d_movie in d["watched"]:           
                if d_movie["title"] in set_movie_title and d_movie not in friends_unique_watched:
                    friends_unique_watched.append(d_movie)

    return   friends_unique_watched

# def get_friends_unique_watched(user_data):
#     friends_unique_watched = []
#     duplicate = False
#     for movie in (user_data["watched"]):
#         duplicate = False
#         for n in range(len(user_data["friends"])):
#             for m in range(len(user_data["friends"][n]["watched"])):
#                 if user_data["friends"][n]["watched"][m]["title"] == movie["title"]:
#                     duplicate = True
#                     break
#             if duplicate:
#                 break
#         if not duplicate: 
#             friends_unique_watched.append(user_data["friends"][n]["watched"][m])

#     return   friends_unique_watched

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

