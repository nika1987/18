from dao.genre_dao import GenreDao
from db_setup.models import GenreSchema


class GenreService:
    def __init__(self, dao: GenreDao):
        self.dao = dao

    def get_one_genre(self, genre_id: int) -> GenreSchema:
        try:
            one_genre = self.dao.get_by_id(genre_id)
            return GenreSchema().dump(one_genre)
        except Exception as e:
            print(e)
            return {}

    def get_all_genre(self):
        try:
            all_genres = self.dao.get_all_genres()
            return GenreSchema(many=True).dump(all_genres)
        except Exception as e:
            print(e)
            return []
