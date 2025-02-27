from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import User
from schemas import UserSchema

user_blp = Blueprint('Users', __name__, description='Operations on users', url_prefix='/users')

@user_blp.route('/')
class UserList(MethodView):
    """
    def get(self):
        users = User.query.all()
        user_data = [{"id":user.id, "name": user.name, "email": user.email} for user in users]  # Convert to list
        return jsonify(user_data)
    """
    @user_blp.response(200,schema=UserSchema(many=True))#직렬화(객체->JSON으로 변환 한다는 뜻)
    def get(self):
        users = User.query.all()
        return users
    """
    def post(self):
        user_data = request.json
        new_user = User(name=user_data['name'], email=user_data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created"}), 201
    """
    @user_blp.arguments(UserSchema)
    @user_blp.response(201,schema=None)
    def post(self,user_data):
        new_user = User(name=user_data['name'], email=user_data['email'])
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created"}
    
@user_blp.route('/<int:user_id>')
class Users(MethodView):
    """
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {"name": user.name, 'email': user.email}
    """
    @user_blp.response(200,schema=UserSchema())
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user
    """
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        user_data = request.json

        user.name = user_data['name']
        user.email = user_data['email']

        db.session.commit()
        return {"message": "User updated"}
    """
    @user_blp.arguments(UserSchema)
    @user_blp.response(200,schema=None)
    def put(self, user_id,user_data):
        user = User.query.get_or_404(user_id)
        user.name = user_data['name']
        user.email = user_data['email']
        db.session.commit()
        return {"message": "User updated"}

    """
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}
    """
    @user_blp.response(200,schema=None)
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}