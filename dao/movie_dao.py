from db_setup.models import Movie


class MovieDaO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        """
        метод получает все фильмы
        """
        return self.session.query(Movie).all()

    def one_movie(self, movie_id):
        """
        метод получает фильм по id
        """
        entity = self.session.query(Movie).get(movie_id)
        return entity

    def get_by_director_id(self, director_id):
        """
        метод получает все фильмы режиссера по id

        """
        result = self.session.query(Movie).filter(Movie.director_id == director_id).all()
        return result

    def get_by_genre_id(self, genre_id):
        """
        метод получает все фильмы жанра

        """
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year):
        """
        метод получает все фильмы за год в формате YEAR
        """
        return self.session.query(Movie).filter(Movie.year == year).all()

    def add_movie(self, movie):
        """
        метод создаем фильм
        """
        new_movie = Movie(**movie)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update_movie(self, movie):
        """
        метод обновляем фильм
        """
        self.session.query(Movie).filter(
            Movie.id == movie['id']
        ).update(movie, synchronize_session='fetch')
        self.session.commit()
        return "Успешно обновлен"

    def delete_movie(self, movie_id):
        """
        метод для удаления фильма
        """
        movie_to_delete = self.session.query(Movie).get(movie_id)
        self.session.delete(movie_to_delete)
        self.session.commit()
