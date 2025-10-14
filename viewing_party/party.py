# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    if not (title and genre and rating):
        return None
    
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    
    return movie

def add_to_watched(user_data, movie):


    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
 
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"] . append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# ------------- WAVE 2 --------------------


def get_watched_avg_rating(user_data):
    total_rating = 0
    average_rating = 0

    if not user_data["watched"]:
        return average_rating
    
    for movie in user_data["watched"]:
        total_rating += movie["rating"]

    average_rating = total_rating / len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    genere_dict = {}

    if not user_data["watched"]:
        return None
    
    for movie in user_data["watched"]:
        genere_dict[movie["genre"]] = genere_dict.get(movie["genre"],0) + 1

    max_genere = ["genere", -1000]

    for genere_key, genere_value in genere_dict.items():
        if genere_value > max_genere[1]:
            max_genere = [genere_key, genere_value]

    return max_genere[0]


# ------------- WAVE 3 --------------------


def get_unique_watched(user_data):
    friends_titles = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_titles.add(movie["title"])
    
    unique_watched = []
    for movie in user_data["watched"]:
        if movie["title"] not in friends_titles:
            unique_watched.append(movie)
    
    return unique_watched

def get_friends_unique_watched(user_data):
    user_titles = set(movie["title"] for movie in user_data["watched"])
    
    friends_unique_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_titles and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
    
    return friends_unique_watched





# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    avalable_recs = []
    recs = get_friends_unique_watched(user_data)

    for rec in recs:
        if rec["host"] in user_data["subscriptions"]:
            avalable_recs.append(rec)

    return avalable_recs


# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):
    new_rec_by_genre = []
    recs = get_friends_unique_watched(user_data)
    most_frequent_genre = get_most_watched_genre(user_data)

    for rec in recs:
        if rec["genre"] == most_frequent_genre:
            new_rec_by_genre.append(rec)

    return new_rec_by_genre

def get_rec_from_favorites(user_data):
    rec_from_favorites = []
    uni_movie = get_unique_watched(user_data)

    for rec in user_data["favorites"]:
        if rec in uni_movie:
            rec_from_favorites.append(rec)

    return rec_from_favorites