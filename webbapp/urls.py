from django.urls import path
from . import views
# app_name = 'webbapp'
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_new_record/', views.add_new_record, name='add_new_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

]
