import requests
import json

# TMDB API key - replace with your own key
api_key = 'f7f8a6afd147937c00947c5ba03655d4'

def get_all_movies():
    # TMDB API endpoint and parameters
    base_url = 'https://api.themoviedb.org/3/'
    endpoint = 'movie/popular'  # You can change this endpoint based on your requirements

    all_movies = []

    # Loop through pages to get data
    for page in range(1, 501):  # Adjust the range as needed
        params = {'api_key': api_key, 'language': 'ko-KR', 'page': page}
        response = requests.get(f'{base_url}{endpoint}', params=params)

        if response.status_code == 200:
            data = response.json()
            for movie in data.get('results', []):
                
                movie_data = {
                    "model": "movies.movie",
                    "pk": movie['id'],
                    "fields": {
                        "adult": movie['adult'],
                        "backdrop_path": movie['backdrop_path'],
                        "genres": movie['genre_ids'],
                        "id": movie['id'],
                        # "original_language": movie['original_language'],
                        # "original_title": movie['original_title'],
                        "overview": movie['overview'],
                        "popularity": movie['popularity'],
                        "poster_path": movie['poster_path'],
                        # "release_date": movie['release_date'],
                        "title": movie['title'],
                        # "video": movie['video'],
                        "vote_average": movie['vote_average'],
                        "vote_count": movie['vote_count']
                    }
                }
                all_movies.append(movie_data)
            print(f'Page {page} success')
        else:
            print(f'Page {page} error: {response.status_code}')

    # Save JSON data to a file
    with open('movie.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_movies, json_file, ensure_ascii=False, indent=2)
    print('All pages data successfully saved.')

# Get all movie data and save it to a file
get_all_movies()
