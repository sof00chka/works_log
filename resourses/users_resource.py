from os import abort

from data import db_session
from data.users import User
from flask import jsonify
from flask_restful import Resource, reqparse


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(User).get(news_id)
    if not news:
        abort(404, message=f"User {news_id} not found")


class UsersResource(Resource):
        def get(self, user_id):
            abort_if_news_not_found(user_id)
            session = db_session.create_session()
            user = session.get(User, user_id)
            return jsonify({'user': user.to_dict(
                only=('surname', "name", 'age', 'position', 'speciality', 'address', 'email', 'modified_date'))})

        def delete(self, news_id):
            abort_if_news_not_found(news_id)
            session = db_session.create_session()
            user = session.get(User, news_id)
            session.delete(user)
            session.commit()
            return jsonify({'success': 'OK'})

parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('content', required=True)
parser.add_argument('is_private', required=True, type=bool)
parser.add_argument('user_id', required=True, type=int)
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)
parser.add_argument('modified_date', required=True)


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('surname', "name", 'age', 'position', 'speciality', 'address')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            adress=args['adress'],
        )
        session.add(users)
        session.commit()
        return jsonify({'id': users.id})