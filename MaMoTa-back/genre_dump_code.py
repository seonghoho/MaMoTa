import requests
import json

# TMDB API 키를 설정합니다. 자신의 키로 교체하세요.
api_key = 'f7f8a6afd147937c00947c5ba03655d4'

def get_all_genres():
    # TMDB API 엔드포인트 및 필요한 매개변수를 설정합니다.
    base_url = 'https://api.themoviedb.org/3/'
    endpoint = 'genre/movie/list'

    all_genres = []

    # 1부터 500까지의 페이지에 대한 데이터를 가져옵니다.
    for page in range(1, 2):
        # language 매개변수를 'ko-KR'로 설정하여 한글 데이터를 가져옵니다.
        params = {'api_key': api_key, 'language': 'ko-KR'}
        response = requests.get(f'{base_url}{endpoint}', params=params)

        # 응답이 성공적인지 확인합니다.
        if response.status_code == 200:
            # JSON 응답을 파싱합니다.
            data = response.json()
            for genre in data.get('genres', []):
                genre_data = {
                    "model": "movies.genre",
                    "pk": genre['id'],
                    "fields": {
                        "name": genre['name']
                    }
                }
                all_genres.append(genre_data)
            print(f'{page} success')
        else:
            print(f' {page} error: {response.status_code}')

    # JSON 데이터를 파일로 저장합니다.
    with open('genre.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_genres, json_file, ensure_ascii=False, indent=2)
    print('모든 페이지의 데이터를 성공적으로 저장했습니다.')

# 모든 페이지의 데이터를 한글로 불러와서 한 파일에 저장합니다.
get_all_genres()