from flask_restx import Resource, Namespace
from container import director_service

directors_ns = Namespace('director', description='Director related operations')


@directors_ns.route('/')
class DirectorList(Resource):
    def get(self):
        all_directors = director_service.get_all_directors()
        return all_directors


@directors_ns.route('/<int:director_id>')
class DirectorDetail(Resource):
    def get(self, director_id):
        one_director = director_service.get_one_director(director_id)
        return one_director
