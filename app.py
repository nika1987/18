

from flask import Flask
from flask_restx import Api

from constants import INSTANCE_PATH
from db_setup.db_create import db
from config import Config

from views.genres.genre_view import genres_ns
from views.directors.director_view import directors_ns
from views.movies.movie_view import movies_ns


# функция создания основного объекта app


def create_app(config_object):
    app = Flask(__name__, instance_path=INSTANCE_PATH)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)

def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)


#
#
# функция

def create_data(app, db):
    with app.app_context():
        db.create_all()


#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#
app = create_app(Config())

#
if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
