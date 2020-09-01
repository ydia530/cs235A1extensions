from domainmodel.movie import Movie
from domainmodel.user import User
from domainmodel.review import Review
from activitysimulations.watchingsimulation import MovieWatchingSimulation


def test_init_watching_simulation():
    user = User("ydia530", '123')
    watching_simulation = MovieWatchingSimulation(user)
    assert watching_simulation.watch_list.size() == 0
    assert watching_simulation.next_playing is None
    assert watching_simulation.now_playing is None
    assert watching_simulation.user == user


def test__watching_simulation_add_movie():
    movie1 = Movie("a", 2020)
    movie2 = Movie("b", 2020)
    movie3 = Movie("c", 2020)
    user = User("ydia530", '123')
    watching_simulation = MovieWatchingSimulation(user)
    watching_simulation.add_movie_to_playlist(movie1)
    watching_simulation.add_movie_to_playlist(movie2)
    watching_simulation.add_movie_to_playlist(movie3)
    assert watching_simulation.watch_list.size() == 3
    assert watching_simulation.now_playing == movie1
    assert watching_simulation.next_playing == movie2


def test_remove_movie_which_playing_now():
    movie1 = Movie("a", 2020)
    movie2 = Movie("b", 2020)
    movie3 = Movie("c", 2020)
    user = User("ydia530", '123')
    watching_simulation = MovieWatchingSimulation(user)
    watching_simulation.add_movie_to_playlist(movie1)
    watching_simulation.add_movie_to_playlist(movie2)
    watching_simulation.add_movie_to_playlist(movie3)
    assert watching_simulation.watch_list.size() == 3
    watching_simulation.remove_movie_from_play_list(movie1)
    assert watching_simulation.watch_list.size() == 2
    assert watching_simulation.now_playing == movie2
    assert watching_simulation.next_playing == movie3


def test_remove_movie_which_is_next_play():
    movie1 = Movie("a", 2020)
    movie2 = Movie("b", 2020)
    movie3 = Movie("c", 2020)
    user = User("ydia530", '123')
    watching_simulation = MovieWatchingSimulation(user)
    watching_simulation.add_movie_to_playlist(movie1)
    watching_simulation.add_movie_to_playlist(movie2)
    watching_simulation.add_movie_to_playlist(movie3)
    assert watching_simulation.watch_list.size() == 3
    watching_simulation.remove_movie_from_play_list(movie2)
    assert watching_simulation.watch_list.size() == 2
    assert watching_simulation.now_playing == movie1
    assert watching_simulation.next_playing == movie3


def test_remove_movie():
    movie1 = Movie("a", 2020)
    movie2 = Movie("b", 2020)
    movie3 = Movie("c", 2020)
    user = User("ydia530", '123')
    watching_simulation = MovieWatchingSimulation(user)
    watching_simulation.add_movie_to_playlist(movie1)
    watching_simulation.add_movie_to_playlist(movie2)
    watching_simulation.add_movie_to_playlist(movie3)
    assert watching_simulation.watch_list.size() == 3
    watching_simulation.remove_movie_from_play_list(movie3)
    assert watching_simulation.watch_list.size() == 2
    assert watching_simulation.now_playing == movie1
    assert watching_simulation.next_playing == movie2


def test_play_next_movie_not_at_end_playlist():
    movie1 = Movie("a", 2020)
    movie2 = Movie("b", 2020)
    movie3 = Movie("c", 2020)
    user = User("ydia530", '123')
    watching_simulation = MovieWatchingSimulation(user)
    watching_simulation.add_movie_to_playlist(movie1)
    watching_simulation.add_movie_to_playlist(movie2)
    watching_simulation.add_movie_to_playlist(movie3)
    assert watching_simulation.now_playing == movie1
    assert watching_simulation.next_playing == movie2
    watching_simulation.play_next_movie()
    assert watching_simulation.now_playing == movie2
    assert watching_simulation.next_playing == movie3
    watching_simulation.play_next_movie()
    assert watching_simulation.now_playing == movie3
    assert watching_simulation.next_playing is None


def test_play_next_movie_at_end_playlist():
    movie1 = Movie("a", 2020)
    movie2 = Movie("b", 2020)
    movie3 = Movie("c", 2020)
    user = User("ydia530", '123')
    watching_simulation = MovieWatchingSimulation(user)
    watching_simulation.add_movie_to_playlist(movie1)
    watching_simulation.add_movie_to_playlist(movie2)
    watching_simulation.add_movie_to_playlist(movie3)
    watching_simulation.play_next_movie()
    watching_simulation.play_next_movie()
    assert watching_simulation.now_playing == movie3
    assert watching_simulation.next_playing is None
    watching_simulation.play_next_movie()
    assert watching_simulation.now_playing is None
    assert watching_simulation.next_playing is None


def test_play_previous_not_at_start():
    movie1 = Movie("a", 2020)
    movie2 = Movie("b", 2020)
    movie3 = Movie("c", 2020)
    user = User("ydia530", '123')
    watching_simulation = MovieWatchingSimulation(user)
    watching_simulation.add_movie_to_playlist(movie1)
    watching_simulation.add_movie_to_playlist(movie2)
    watching_simulation.add_movie_to_playlist(movie3)
    watching_simulation.play_next_movie()
    watching_simulation.play_next_movie()
    watching_simulation.play_next_movie()
    watching_simulation.play_previous_movie()
    assert watching_simulation.now_playing == movie3
    assert watching_simulation.next_playing is None
    watching_simulation.play_previous_movie()
    assert watching_simulation.now_playing == movie2
    assert watching_simulation.next_playing == movie3
    watching_simulation.play_previous_movie()
    assert watching_simulation.now_playing == movie1
    assert watching_simulation.next_playing == movie2


def test_play_previous_at_start():
    movie1 = Movie("a", 2020)
    movie2 = Movie("b", 2020)
    movie3 = Movie("c", 2020)
    user = User("ydia530", '123')
    watching_simulation = MovieWatchingSimulation(user)
    watching_simulation.add_movie_to_playlist(movie1)
    watching_simulation.add_movie_to_playlist(movie2)
    watching_simulation.add_movie_to_playlist(movie3)
    watching_simulation.play_previous_movie()
    assert watching_simulation.now_playing == movie1
    assert watching_simulation.next_playing == movie2


def test_review_simulation():
    movie1 = Movie("a", 2020)
    movie2 = Movie("b", 2020)
    movie3 = Movie("c", 2020)
    user = User("ydia530", '123')
    watching_simulation = MovieWatchingSimulation(user)
    watching_simulation.add_movie_to_playlist(movie1)
    watching_simulation.add_movie_to_playlist(movie2)
    watching_simulation.add_movie_to_playlist(movie3)
    watching_simulation.review_to_current_playing_movie()
    assert len(watching_simulation.review) == 1
    watching_simulation.play_next_movie()
    watching_simulation.review_to_current_playing_movie()
    assert len(watching_simulation.review) == 2
    print(watching_simulation.review)


def test_search_movie_to_watch():
    movie1 = Movie("a", 2020)
    movie2 = Movie("b", 2020)
    movie3 = Movie("c", 2020)
    user = User("ydia530", '123')
    watching_simulation = MovieWatchingSimulation(user)
    watching_simulation.add_movie_to_playlist(movie1)
    watching_simulation.add_movie_to_playlist(movie2)
    watching_simulation.add_movie_to_playlist(movie3)
    watching_simulation.search_movie_from_playlist_to_watch(movie2)  # test fot searching movie inside watchlist
    assert watching_simulation.now_playing == movie2
    assert watching_simulation.next_playing == movie3
    watching_simulation.search_movie_from_playlist_to_watch(movie3)  # test for searching movie at end watchlist
    assert watching_simulation.now_playing == movie3
    assert watching_simulation.next_playing is None
    watching_simulation.search_movie_from_playlist_to_watch(Movie("d",2020))  #test for searching movie not in watchlist
    assert watching_simulation.now_playing == movie3
    assert watching_simulation.next_playing is None








