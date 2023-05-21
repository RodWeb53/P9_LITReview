from django.urls import path
from authentication import views

urlpatterns=[
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
]
