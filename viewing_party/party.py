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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

