from dao.director_dao import DirectorDao
from db_setup.models import DirectorSchema


class DirectorService:
    def __init__(self, dao: DirectorDao):
        self.dao = dao

    def get_one_director(self, director_id: int) -> DirectorSchema:
        try:
            one_director = self.dao.get_by_id(director_id)
            return DirectorSchema().dump(one_director)
        except Exception as e:
            print(e)
            return {}

    def get_all_directors(self):
        try:
            all_directors = self.dao.get_all_directors()
            return DirectorSchema(many=True).dump(all_directors)
        except Exception as e:
            print(e)
            return []







