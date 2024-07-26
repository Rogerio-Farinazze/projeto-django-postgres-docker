from django.urls import path
from app.views import index
from . import views

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
