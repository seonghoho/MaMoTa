# 2023-11-14

1. piniaPluginPersistedstate 설치함
2. counter.js 는 언제든 수정 가능 나중에 새로 만들 때 참고할만하게 완전 스켈레톤 코드만 적어놓음
3. NavBar에 대해 기본적인 Bootstrap만 설치 해놓음 (나중에 vuetify 활용해서 수정 예정)
4. .env에 우선 김선욱 TMDB api 작성 해둠 (인기순으로 우선 불러왔는데 나중에 수정할 예정)
5. 필수 설치 사항
   - npm install bootstrap
   - npm install bootstrap-icons
   - npm install axios
   - npm i pinia-plugin-persistedstate
   - npm install vue3-youtube
   - npm install youtube-iframe
   - npm install -D sass
   - npm install vuex

# 2023-11-15

## 김선욱
- TMDB 인기순 평점순 HomeView에 분기 나눔
- TMDB 인기순 평점순 API 따로 받아옴
- RouterLink로 연결시킴
- 기선이 사진 누르면 Home으로 감

## 최성호
- Django project 생성
- accounts app, movies app 생성
- back 기본 구조 설정

- 디테일 페이지 작성

# 2023-11-16

## 김선욱
- Movie Detail 페이지 모달로 바로 Movie 전체 페이지에서 출력 가능하게 함
- 유튜브 트레일러 구현중... (아직 API 할당량 문제 해결 못함)
- 검색 기능창 구현 중... (아직 Axios 에러)
- OpenAI 모달 구현 중... (아직 Axios 에러)
- 스크롤 바 제일 위로 올리기 구현 완료

## 최성호
- movies app model 생성
- serializers and views 수정
- community app 수정중..

# 2023-11-17

## 최성호
- community app 수정


## 오기선
- community 전체 틀 페이지 생성
- ArticleListView 작성
- ArticleDetailView 작성
- CommentList 작성
- CommentCreate 구현중...(Axios 호출 주석처리)
- admin 페이지로 들어가 데이터 생성 시 확인가능
- 