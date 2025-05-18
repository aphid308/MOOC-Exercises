class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.genre_string = ", ".join(genres)
        self.ratings = []

    def rate(self, rating: int):
        self.ratings.append(rating)


    def __str__(self):
        if self.ratings:
            ratings_string = f"{len(self.ratings)} ratings, average {sum(self.ratings) / len(self.ratings)} points"
        else:
            ratings_string = "No ratings"
        return (f"{self.title} ({self.seasons} Seasons)\n"
                f"genres: {self.genre_string}\n"
                f"{ratings_string}" )

def minimum_grade(rating: float, series_list: list):
    rated_series = []
    for s in series_list:
        if sum(s.ratings) / len(s.ratings) >= rating:
            rated_series.append(s)
        else:
            pass
    return rated_series

def includes_genre(genre: str, series_list: list):
    genre_series = []
    for s in series_list:
        if genre in s.genres:
            genre_series.append(s)
        else:
            pass
    return genre_series

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)