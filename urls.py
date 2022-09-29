from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>', views.userProfile, name="user-profile"),

    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    # path('project/<str:pk>', views.project, name="project"),
    # path('create-project/', views.createProject, name="create-project"),
    #
    # path('update-project/<str:pk>', views.updateProject, name="update-project"),
    #
    # path('delete-project/<str:pk>', views.deleteProject, name="delete-project"),

]