from domainmodel.watchlist import WatchList
from domainmodel.movie import Movie


def test_init_watchlist():
    watchlist = WatchList()
    assert f"Size of watchlist: {watchlist.size()}" == "Size of watchlist: 0"
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    assert f"Size of watchlist: {watchlist.size()}" == "Size of watchlist: 3"


def test_check_size():
    watchlist = WatchList()
    assert f"Size of watchlist: {watchlist.size()}" == "Size of watchlist: 0"
    watchlist.add_movie(Movie("a", 2012))
    watchlist.add_movie(Movie("a", 2012))
    assert f"Size of watchlist: {watchlist.size()}" == "Size of watchlist: 1"


def test_check_size_of_nonempty_watchlist():
    watchlist = WatchList()
    assert f"Size of watchlist: {watchlist.size()}" == "Size of watchlist: 0"


def test_add_movie():
    watchlist = WatchList()
    watchlist.add_movie(Movie("a", 2012))
    assert f"Size of watchlist: {watchlist.size()}" == "Size of watchlist: 1"


def test_add_same_movie_again():
    watchlist = WatchList()
    watchlist.add_movie(Movie("a", 2012))
    watchlist.add_movie(Movie("a", 2012))
    assert f"Size of watchlist: {watchlist.size()}" == "Size of watchlist: 1"


def test_remove_movie_which_is_not_in_watchlist():
    watchlist = WatchList()
    watchlist.add_movie(Movie("a", 2012))
    watchlist.remove_movie(Movie("b", 2010))
    assert f"Size of watchlist: {watchlist.size()}" == "Size of watchlist: 1"


def test_select_movie_to_watch_index_out_of_bounds():
    watchlist = WatchList()
    watchlist.add_movie(Movie("a", 2012))
    movie = watchlist.select_movie_to_watch(1)
    assert movie is None


def test_iterator_used():
    watchlist = WatchList()
    watchlist.add_movie(Movie("a", 2012))
    i = iter(watchlist)
    assert next(i) == Movie('a', 2012)


def test_iterator_reaches_final_element():
    watchlist = WatchList()
    watchlist.add_movie(Movie("a", 2012))
    i = iter(watchlist)
    for a in i:
        try:
            assert a == Movie("a", 2012)
        except StopIteration:
            pass
