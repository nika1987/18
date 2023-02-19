from db_setup.models import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, director_id):
        """
        метод получает режиссер по id

        """
        return self.session.query(Director).get(director_id)

    def get_all_directors(self):
        """
        метод получает всех режиссеров из базы данных
        """
        return self.session.query(Director).all()
