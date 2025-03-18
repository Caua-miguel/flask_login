# from project import login_manager
# from project.users.views import users
# from database.models import User_ORM

# @login_manager.user_loader
# def user_loader(name):
#     if name not in users:
#         return
    
#     user = User_ORM()
#     user.id = name
#     return user

# @login_manager.request_loader
# def request_loader(request):
#     name = request.form.get('name')
#     if name not in users:
#         return
    
#     user = User_ORM()
#     user.id = name
#     return user