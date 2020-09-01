from typing import List
from domainmodel.movie import Movie


class WatchList:
    def __init__(self):
        self.__watch_list : List[Movie] = list()

    def add_movie(self, movie: Movie):
        if movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.__watch_list:
            self.__watch_list.remove(movie)

    def size(self):
        return len(self.__watch_list)

    def select_movie_to_watch(self, index: int):
        if index < self.size():
            return self.__watch_list[index]
        else:
            return None

    def first_movie_in_watchlist(self):
        if self.size() == 0:
            return None
        else:
            return self.__watch_list[0]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.size():
            movie = self.__watch_list[self.index]
            self.index += 1
            return movie
        else:
            raise StopIteration


