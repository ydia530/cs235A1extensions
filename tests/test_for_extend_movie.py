from domainmodel.movie import Movie


def test_for_extend_movie_vote():
    movie = Movie("a", 2016)
    assert movie.votes is None
    movie.votes = -10
    assert movie.votes is None
    movie.votes = 200
    assert movie.votes == 200
    movie.votes_the_movie()
    assert movie.votes == 201


def test_for_extend_movie_revenue():
    movie = Movie("a", 2016)
    assert movie.revenue == 'N/A'
    movie.revenue = -235
    assert movie.revenue == 'N/A'
    movie.revenue = 235.0
    assert movie.revenue == 235.0


def test_for_extend_movie_metascore():
    movie = Movie("a", 2016)
    assert movie.metascore is None
    movie.metascore = -10
    assert movie.metascore is None
    movie.metascore = 101
    assert movie.metascore is None
    movie.metascore = 99
    assert movie.metascore == 99



