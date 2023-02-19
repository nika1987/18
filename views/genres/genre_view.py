from flask_restx import Resource, Namespace
from container import genre_service

genres_ns = Namespace('genres', description='Genre related operations')


@genres_ns.route('/')
class GenreList(Resource):
    def get(self):
        all_genres = genre_service.get_all_genre()
        return all_genres


@genres_ns.route('/<int:genre_id>')
class GenreDetail(Resource):
    def get(self, genre_id):
        one_genre = genre_service.get_one_genre(genre_id)
        return one_genre
