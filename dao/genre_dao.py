from db_setup.models import Genre


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, genre_id):
        """
        метод получение объекта по id
        """
        return self.session.query(Genre).get(genre_id)

    def get_all_genres(self):
        """
        метод получение всех жанров

        """
        return self.session.query(Genre).all()
