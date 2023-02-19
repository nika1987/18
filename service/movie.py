from dao.movie_dao import MovieDaO
from db_setup.models import MovieSchema


class MovieService:
    def __init__(self, dao: MovieDaO):
        self.dao = dao

    def get_all_movies(self):
        try:
            data = self.dao.get_all_movies()
            print(data)
            return MovieSchema(many=True).dump(data)
        except Exception as e:
            print(e)
            return []

    def one_movie(self, movie_id):
        try:
            one_movie = self.dao.one_movie(movie_id)
            return MovieSchema().dump(one_movie)
        except Exception as e:
            print(e)
            return "Такой фильм не найден"

    def get_by_director_id(self, director_id):
        try:
            movies = self.dao.get_by_director_id(director_id)
            return MovieSchema(many=True).dump(movies)
        except Exception as e:
            print(e)
            return []

    def get_by_genre_id(self, genre_id):
        try:
            movies = self.dao.get_by_genre_id(genre_id)
            return MovieSchema(many=True).dump(movies)
        except Exception as e:
            print(e)
            return []

    def get_by_year(self, year):
        try:
            movies = self.dao.get_by_year(year)
            return MovieSchema(many=True).dump(movies)
        except Exception as e:
            print(e)
            return []

    def add_movie(self, movie):
        try:
            new_movie = self.dao.add_movie(movie)
            return MovieSchema().dump(new_movie)
        except Exception as e:
            print(e)
            return "Не удалось добавить фильм"

    def update_movie(self, movie):
        try:
            result = self.dao.update_movie(movie)
            return result
        except Exception as e:
            print(e)
            return "Не удалось обновить фильм"

    def delete_movie(self, movie_id):
        try:
            self.dao.delete_movie(movie_id)
            return "Удалено успешно"
        except Exception as e:
            print(e)
            return "Не удалось удалить фильм"
