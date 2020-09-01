from datetime import datetime
from domainmodel.movie import Movie


class Review:
    def __init__(self, movie:Movie, review_text: str, rating: int):
        if type(movie) == Movie:
            self.__movie = movie
        else:
            self.__movie = None
        if type(review_text) == str:
            self.__review_text = review_text.strip()
        else:
            self.__review_text = None
        if type(rating) == int and 1 <= rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp: datetime = datetime.now()

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return f'<{self.__movie} {self.__timestamp}>'

    def __eq__(self, other):
        if not isinstance(other,Review):
            return False
        return (
            other.__timestamp == self.__timestamp and
            other.__movie == self.__movie and
            other.__review_text == self.__review_text and
            other.__rating == self.__rating
        )

