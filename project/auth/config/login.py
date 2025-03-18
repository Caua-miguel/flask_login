from project import login_manager
from database.models import User_ORM, db

@login_manager.user_loader
def user_loader(email):

    users = db.session.query(User_ORM).all()
    user = User_ORM.query.filter_by(email=email).first()

    if email not in users:
        return
    
    return user

@login_manager.request_loader
def request_loader(request):
    
    email = request.form.get('email')

    users = db.session.query(User_ORM).all()
    user = User_ORM.query.filter_by(email=email).first()

    
    if email not in users:
        return
    
    return user