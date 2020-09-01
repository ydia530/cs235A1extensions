from typing import List, Iterable
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:
    def __init__(self, title: str, year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title: str = title.strip()
        if year < 1900:
            self.__release_year = None
        else:
            if type(year) == int:
                self.__release_year: int = year
            else:
                self.__release_year: int = None

        self.__description = None
        self.__director = None
        self.__actors: List[Actor] = list()
        self.__genres: List[Genre] = list()
        self.__runtime_minutes = None
        self.__votes = None
        self.__revenue = 'N/A'
        self.__metascore = None

    @property
    def title(self) -> str:
        return self.__title

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, descrip: str):
        if type(descrip) == str:
            self.__description = descrip.strip()

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, d: Director):
        if type(d) == Director:
            self.__director = d

    @property
    def actors(self) -> Iterable["Actor"]:
        return self.__actors

    @actors.setter
    def actors(self, actor: Actor):
        if type(actor) == Actor:
            self.__actors.append(actor)

    @property
    def genres(self) -> Iterable["Genre"]:
        return self.__genres

    @genres.setter
    def genres(self, genre: Genre):
        if type(genre) == Genre:
            self.__genres.append(genre)

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, time: int):
        if type(time) == int and time >= 0:
            self.__runtime_minutes = time
        else:
            raise ValueError

    @property
    def votes(self) -> int:
        return self.__votes

    @votes.setter
    def votes(self, vote: int):
        if type(vote) == int and vote >= 0:
            self.__votes = vote

    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, revenue: float):
        if type(revenue) == float and revenue >= 0:
            self.__revenue = revenue

    @property
    def metascore(self) -> int:
        return self.__metascore

    @metascore.setter
    def metascore(self, score: int):
        if type(score) == int and 0 <= score <= 100:
            self.__metascore = score

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        if self.__title == other.title and self.__release_year == other.release_year:
            return True
        return False

    def __lt__(self, other):
        if type(other) == Movie:
            if self.__title == other.title:
                return self.__release_year < other.release_year
            else:
                return self.__title < other.title

    def __hash__(self):
        return hash(self.__title+str(self.__release_year))

    def add_actor(self, actor: Actor):
        if type(actor) == Actor:
            self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        for a in self.__actors:
            if a == actor:
                self.__actors.remove(a)

    def add_genre(self, genre: Genre):
        if type(genre) == Genre:
            self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        for a in self.__genres:
            if a == genre:
                self.__genres.remove(a)

    # interface for user voting the movie.
    def votes_the_movie(self):
        self.__votes += 1

