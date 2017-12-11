import webbrowser


# Movie Class that supports required functionality
class Movie(object):
    # This is the Constructor that initializes the object in memory
    def __init__(self,
                 movie_title,
                 story_line,
                 poster_image_url,
                 trailer_youtube_id):
        # Instace Variables
        self.title = movie_title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_id

    def show_trailer(self):
        # Function to open a trailer
        webbrowser.open(self.trailer_youtube_id)
