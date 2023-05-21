from django.urls import path
from ticket import views

urlpatterns=[
    path('home/', views.home, name='home'),
    
    path('ticket/add/', views.add_ticket, name='create_ticket'),
    path('ticket/update/<int:ticket_id>/', views.add_ticket, name="update_ticket"),
    
    path('ticket/delete/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
    
    
    path('review/add/', views.create_review, name="create_review"),
    path('ticket/add/review/<int:ticket_id>', views.create_review_in_ticket, name='create_review_in_ticket'),
    path('review/update/<int:review_id>/', views.update_review, name="update_review"),
    path('review/delete/<int:review_id>/', views.delete_review, name="delete_review"),
    
    path("ticket/posts/", views.posts, name='posts'),
]
