# The fresh_tomatoes.py module has a function called open_movies_page
# that takes in one argument, as a list of movies, and creates
# an HTML file that in-turn display the movies from the list.

# In order to create the multple object from the the class Movie,
# we need to import the python file media.py.
import fresh_tomatoes
import media

# movieList is a array of instances of class Movie
# First is created empty list
movieList = []

# Than multiple instacnes are append to the movie list
movieList.append(media.Movie("Batman vs. Superman",
                 'Fearing that the actions of Superman are left unchecked, ' +
                 'Batman takes on the Man of Steel, while the world ' +
                 'wrestles with what kind of a hero it really needs.',
                 "https://img.csfd.cz/files/images/film/posters/160/463/160463887_e205cb.jpg",  # NOQA
                 "https://www.youtube.com/watch?v=m8KWFUqrlCI"))  # NOQA
movieList.append(media.Movie("Avatar",
                 "A paraplegic marine dispatched to the moon Pandora on a " +
                 "unique mission becomes torn between following his orders " +
                 "and protecting the world he feels is his home.",
                 "https://img.csfd.cz/files/images/film/posters/158/597/158597600_9917dd.jpg?h180",  # NOQA
                 "https://www.youtube.com/watch?v=f5-wECt6A6o"))  # NOQA
movieList.append(media.Movie("Gladiator",
                 "When a Roman General is betrayed, and his family murdered " +
                 "by an emperor's corrupt son, he comes to Rome as a " +
                 "gladiator to seek revenge. ",
                 "https://img.csfd.cz/files/images/film/posters/159/217/159217194_e183d5.jpg?h180",  # NOQA
                 "https://www.youtube.com/watch?v=PelNjR2T1Lg"))  # NOQA
movieList.append(media.Movie("Forest Gump",
                 "JFK, LBJ, Vietnam, Watergate, and other history unfold " +
                 "through the perspective of an Alabama man with an IQ of 75.",
                 "https://img.csfd.cz/files/images/film/posters/158/988/158988468_acc7b5.jpg?h180",  # NOQA
                 "https://www.youtube.com/watch?v=oLPRB_CriEo"))  # NOQA
movieList.append(media.Movie("Home Alone",
                 "An eight-year-old troublemaker must protect his house " +
                 "from a pair of burglars when he is accidentally left " +
                 "home alone by his family during Christmas vacation.",
                 "https://img.csfd.cz/files/images/film/posters/158/724/158724678_92fe35.jpg?h180",  # NOQA
                 "https://www.youtube.com/watch?v=rQZfCd9BOJE"))  # NOQA
movieList.append(media.Movie("Three Wishes for Cinderella",
                 "Life changes dramatically for a Czech housemaid when " +
                 "the house driver gives her three magical hazel nuts. ",
                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg3NDEyNDM4NF5BMl5BanBnXkFtZTcwMzM2MzQyMQ@@._V1_.jpg",  # NOQA
                 "https://www.youtube.com/watch?v=aA0D57uIZ_0&t=21s"))  # NOQA

# Uppon passing movie list to the function open_movies_page
# in the fresh_tomatoes module, HTML file is generated with this list
fresh_tomatoes.open_movies_page(movieList)
