from project import login_manager
from database.models import users, User

@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return
    
    user = User()
    user.id = username
    return user

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    if username not in users:
        return
    
    user = User()
    user.id = username
    return user