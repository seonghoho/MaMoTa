from django.urls import path
from . import views


app_name = 'community'
urlpatterns = [
    path('', views.article_list),
    path('article/', views.article_create),
    path('article/<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/like/', views.article_like),
    
    path('comments/', views.comment_list),
    path('article/<int:article_pk>/comments/', views.comment_create),    
    path('article/<int:article_pk>/comments/<int:comment_pk>/', views.comment_delete),
]
