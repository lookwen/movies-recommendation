class Movie:
    def __init__(self, _id : int, title : str, genres : list[str], description : str, rating : float, poster : str):
        self.id = _id
        self.title = title
        self.genres = genres
        self.description = description
        self.rating = rating
        self.poster = poster

        