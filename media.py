# cook your code here
import webbrowser


class Movie():
    """
        title(args) --> It contains the title of the movie.
        storyline(args)--> it contains description of the movie.
        poster_image_url --> Link of the movie poster.
        trailer_youtube_url -> Youtube link to the trailer of the movie."""
    VALID_RATINGS = ["G", "PG", "PG 13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
    			"""This describes the constructor method, which provides
                us with input and output."""
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This tells us about what show_trailer function does"""
        webbrowser.open(self.trailer_youtube_url)
