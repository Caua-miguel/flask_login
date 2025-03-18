from project import login_manager
from database.models import User_ORM, db

@login_manager.user_loader
def user_loader(name):

    users = db.session.query(User_ORM).all()

    if name not in users:
        return
    
    user = User_ORM()
    user.id = name
    return user

@login_manager.request_loader
def request_loader(request):

    users = db.session.query(User_ORM).all()

    name = request.form.get('name')
    if name not in users:
        return
    
    user = User_ORM()
    user.id = name
    return user