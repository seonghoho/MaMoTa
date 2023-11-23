from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/addlist/', views.add_list),
    
    
    # # 명대사 주소
    # path('<int:movie_pk>/famous_lines/', views.famous_line_list),
    # path('<int:movie_pk>/famous_lines/create/', views.famous_line_create),
    # path('<int:movie_pk>/famous_lines/<int:famous_line_pk>/', views.famous_line_detail),
    
    # # 리뷰 주소
    # path('<int:movie_pk>/reviews/', views.review_list),
    # path('<int:movie_pk>/reviews/create/', views.review_create),
    # path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail),
    
]