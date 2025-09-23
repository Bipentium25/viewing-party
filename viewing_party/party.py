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

 

    




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

