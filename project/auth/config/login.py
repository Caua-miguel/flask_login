from project import login_manager
from database.models import User_ORM

@login_manager.user_loader
def user_loader(user_id):
    user = User_ORM.query.filter_by(id=user_id).first()

    if not user:
        return

    return user

@login_manager.request_loader
def request_loader(request):
    
    id = request.form.get('id')
    user = User_ORM.query.filter_by(id=id).first()
    
    if not user:
        return
    
    return user