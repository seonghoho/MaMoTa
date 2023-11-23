from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# from django.core.paginator import Paginator
# from django.db.models import Count
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import (
    MovieListSerializer,
    MovieSerializer,
    # MovieGenreSerializer,
    # FamousLineSerializer,
    # ReviewSerializer
)
from .models import Movie


# 모든 영화
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


# 각 영화별 detail 정보
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializr = MovieSerializer(movie)
    return Response(serializr.data)


# user가 add list 한 목록
@api_view(['POST'])
def add_list(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)



# # 명대사 리스트
# @api_view(['GET'])
# def famous_line_list(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     famous_lines = movie.famous_lines.all()
#     serializer = FamousLineSerializer(famous_lines, many=True)
#     return Response(serializer.data)


# # 명대사 생성
# @api_view(['POST'])
# # @permission_classes([IsAuthenticated])
# def famous_line_create(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = FamousLineSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(movie=movie, user=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# # 명대사 수정, 삭제
# @api_view(['PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def famous_line_detail(request, famous_line_pk):
#     famous_line = get_object_or_404(FamousLine, pk=famous_line_pk)

#     # 댓글 삭제
#     if request.method == 'DELETE':
#         if request.user == famous_line.user: 
#             famous_line.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

#     # 댓글 수정
#     elif request.method == 'PUT':
#         if request.user == famous_line.user: 
#             serializer = FamousLineSerializer(famous_line, data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data)
            
      
      
            
# # 리뷰 리스트
# @api_view(['GET'])
# def review_list(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     reviews = movie.reviews.all()
#     serializer = ReviewSerializer(reviews, many=True)
#     return Response(serializer.data)


# # 리뷰 생성
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def review_create(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = ReviewSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(movie=movie, user=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# # 리뷰 수정, 삭제
# @api_view(['PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def review_detail(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)

#     # 댓글 삭제
#     if request.method == 'DELETE':
#         if request.user == review.user: 
#             review.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

#     # 댓글 수정
#     elif request.method == 'PUT':
#         if request.user == review.user: 
#             serializer = ReviewSerializer(review, data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data)