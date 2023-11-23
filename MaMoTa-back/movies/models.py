from django.db import models
from django.conf import settings

# import datetime

# class Actor(models.Model):
#     name = models.CharField(max_length=50, null=False)
#     profile_path = models.TextField(null=True)

#     def __str__(self):
#         return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    # actors = models.ManyToManyField(Actor, related_name='movies')
    
    adult = models.BooleanField(null=True)
    backdrop_path = models.CharField(max_length=300, null=True)
    title = models.CharField(max_length=300)
    overview = models.TextField(null=True)
    # budget = models.BigIntegerField()
    popularity = models.FloatField(null=True)
    poster_path = models.TextField(null=True)
    # release_date = models.DateField(null=True, default=datetime.date.today)
    # revenue = models.BigIntegerField()
    # runtime = models.IntegerField(null=True)
    # tagline = models.TextField(null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    # words = models.TextField(null=True)
    
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_movies'
    )

    def __str__(self):
        return self.title


# # 명대사
# class FamousLine(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='famous_lines',
#     )
#     movie = models.ForeignKey(
#         Movie, on_delete=models.CASCADE, related_name='famous_lines'
#     )
#     content = models.CharField(max_length=300)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



# # 한 줄 리뷰
# class Review(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='reviews',
#     )
#     movie = models.ForeignKey(
#         Movie, on_delete=models.CASCADE, related_name='reviews'
#     )
#     content = models.CharField(max_length=300)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
