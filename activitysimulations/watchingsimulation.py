from domainmodel.movie import Movie
from domainmodel.user import User
from domainmodel.review import Review
from domainmodel.watchlist import WatchList


class MovieWatchingSimulation:
    def __init__(self, user: User):
        if type(user) == User:
            self.__user = user
        else:
            self.__user = None
        self.__watch_list = WatchList()
        self.__now_playing = None
        self.__next_playing = None
        self.__play_pointer = 0
        self.__review = list()

    @property
    def user(self):
        return self.__user

    @property
    def watch_list(self):
        return self.__watch_list

    @property
    def now_playing(self):
        return self.__now_playing

    @property
    def next_playing(self):
        return self.__next_playing

    @property
    def review(self):
        return self.__review

    def add_movie_to_playlist(self, movie: Movie):
        if movie not in self.__watch_list and type(movie) ==Movie:
            if self.__watch_list.size() == 0:
                self.__watch_list.add_movie(movie)
                self.__now_playing = movie
                self.__play_pointer = 0
            else:
                if self.__watch_list.size() == 1:
                    self.__next_playing = movie
                    self.__watch_list.add_movie(movie)
                else:
                    self.__watch_list.add_movie(movie)

    def remove_movie_from_play_list(self, movie: Movie):
        if movie == self.__now_playing:
            self.__now_playing = self.__next_playing
            self.__watch_list.remove_movie(movie)
            self.__next_playing = self.__watch_list.select_movie_to_watch(self.__play_pointer+1)
        elif movie == self.__next_playing:
            self.__watch_list.remove_movie(movie)
            self.__next_playing = self.__watch_list.select_movie_to_watch(self.__play_pointer+1)
        else:
            self.__watch_list.remove_movie(movie)

    def play_next_movie(self):
        if self.__play_pointer + 1 < self.__watch_list.size():
            self.__play_pointer += 1
            self.__now_playing = self.__watch_list.select_movie_to_watch(self.__play_pointer)

            if self.__play_pointer + 1 < self.__watch_list.size():
                self.__next_playing = self.__watch_list.select_movie_to_watch(self.__play_pointer+1)
            else:
                self.__next_playing = None

        else:
            self.__now_playing = None
            self.__play_pointer += 1

    def play_previous_movie(self):
        if self.__play_pointer == self.__watch_list.size():
            self.__play_pointer -= 1
            self.__now_playing = self.__watch_list.select_movie_to_watch(self.__play_pointer)
        elif self.__play_pointer - 1 >= 0:
            self.__play_pointer -= 1
            self.__now_playing = self.__watch_list.select_movie_to_watch(self.__play_pointer)
            self.__next_playing = self.__watch_list.select_movie_to_watch(self.__play_pointer+1)
        else:
            pass

    def review_to_current_playing_movie(self):

        # Simulate user input for test only. Request input later on.
        review = Review(self.__now_playing, "Good Movie, I like it.", 10)
        self.__review.append(review)

    def search_movie_from_playlist_to_watch(self, movie: Movie):
        i = 0
        for m in self.__watch_list:
            if movie == m:
                self.__now_playing = movie
                self.__play_pointer = i
                self.__next_playing = self.__watch_list.select_movie_to_watch(i+1)
                break
            i += 1





















