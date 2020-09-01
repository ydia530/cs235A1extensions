from typing import List

from domainmodel.movie import Movie
from domainmodel.review import Review


class User:
    def __init__(self, user_name: str, password: str):
        if type(user_name) == str:
            self.__user_name = user_name.lower().strip()
        else:
            self.__user_name = None
        if type(password) == str:
            self.__password = password
        else:
            self.__password = None
        self.__watched_movies: List[Movie] = list()
        self.__reviews: List[Review] = list()
        self.__time_spend_watching_movies_minutes: int = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spend_watching_movies_minutes

    def __repr__(self):
        return f'<User {self.__user_name}>'

    def __eq__(self, other):
        return self.__user_name == other.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie: Movie):
        if type(movie) == Movie:
            self.__watched_movies.append(movie)
            self.__time_spend_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review:Review):
        if type(review) == Review:
            self.__reviews.append(review)



user1 = User('Martin', 'pw12345')
user2 = User('Ian', 'pw67890')
user3 = User('Daniel', 'pw87465')
print(user1)
print(user2)
print(user3)