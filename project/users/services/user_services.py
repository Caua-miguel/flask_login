from flask import  request
from project import bcrypt
from database.config.db import db
from database.models.users import Users
class User:

    def select_users():
        users = db.session.query(Users).all()
        users_list = [user.as_dict() for user in users]
        return users_list
    
    def user_exists():
        data = request.get_json()
        user_exists = Users.query.filter_by(email=data['email']).first() is not None
        return user_exists
    
    def user_by_id(id):
        user_by_id = db.get_or_404(Users, id)
        return user_by_id
    
    def insert_user():
        data = request.get_json()
        hash_password = bcrypt.generate_password_hash(data['password'])
        newUser = Users(name=data['name'], age=data['age'], email=data['email'], password=hash_password)
        db.session.add(newUser)
        db.session.commit()
        return
    
    def update_user(id):
        data = request.get_json() 
        Users.query.filter_by(id=id).update(data)
        db.session.commit()
        return
    
    def delete_user(id):
        db.session.delete(User.user_by_id(id))
        db.session.commit()
        return
