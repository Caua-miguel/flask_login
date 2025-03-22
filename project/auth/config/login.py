from project import login_manager
from database.models.users import Users

@login_manager.user_loader
def user_loader(user_id):
    user = Users.query.filter_by(id=user_id).first()

    if not user:
        return

    return user

@login_manager.request_loader
def request_loader(request):
    
    id = request.form.get('id')
    user = Users.query.filter_by(id=id).first()
    
    if not user:
        return
    
    return user