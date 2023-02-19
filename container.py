from dao.director_dao import DirectorDao
from dao.genre_dao import GenreDao
from dao.movie_dao import MovieDaO
from db_setup.db_create import db
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService

movie_dao = MovieDaO(db.session)
movie_service = MovieService(movie_dao)
genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)
director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)
