from flask_restx import Resource, Namespace
from container import movie_service
from flask import request
movies_ns = Namespace('movies', description='Movie related operations')


@movies_ns.route('/')
class MoviesList(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        if director_id:
            return movie_service.get_movies_by_director_id(int(director_id))
        elif genre_id:
            return movie_service.get_movies_by_genre_id(int(genre_id))
        elif year:
            return movie_service.get_movies_by_year(int(year))
        all_movies = movie_service.get_all_movies()
        return all_movies

    def post(self):
        movie_data = request.json
        new_movie = movie_service.add_movie(movie_data)
        return new_movie


@movies_ns.route('/<int:movie_id>')
class MovieDetail(Resource):
    def get(self, movie_id):
        single_movie = movie_service.one_movie(movie_id)
        return single_movie

    def put(self, movie_id):
        created_movie = movie_service.update_movie(request.json)
        return created_movie

    def delete(self, movie_id):
        return movie_service.delete_movie(movie_id)
