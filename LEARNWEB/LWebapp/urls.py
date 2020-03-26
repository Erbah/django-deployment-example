from django.urls import path
from LD_app import views

# SET THE NAMESPACE!
app_name = 'LWebapp'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('searchView/',views.searchView,name='searchView' ),
]
