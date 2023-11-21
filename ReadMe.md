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
   - npm install vue3-carousel-3d
   - npm i --save @fortawesome/fontawesome-svg-core
   - npm i --save @fortawesome/free-solid-svg-icons
   - npm i --save @fortawesome/free-regular-svg-icons
   - npm i --save @fortawesome/free-brands-svg-icons
   - npm i --save @fortawesome/vue-fontawesome@3

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
- community app 수정중...


# 2023-11-17

## 김선욱
- 메인 페이지 TMDB API 받아와서 슬라이드 형태로 꾸밈
- 이것밖에 안함 ㅋ

## 최성호
- community app 수정

## 오기선
- community 전체 틀 페이지 생성
- ArticleListView 작성
- ArticleDetailView 작성
- CommentList 작성
- CommentCreate 구현중...(Axios 호출 주석처리)
- admin 페이지로 들어가 데이터 생성 시 확인가능


# 2023-11-19

## 김선욱
- 디테일인포에 장르 띄우기
- 전체적인 테마 블랙 + 퍼플로 변경

## 최성호
- 로그인 커스터마이징 수정
  
## 오기선
- 댓글 수정,삭제 추가


# 2023-11-20

## 김선욱
- 영화 감독, 배우 정보 받아옴
- 영화 Search 페이지 구현
- 영화 사이트 배경 우주 GIF 적용 (아직 고르는 중)
  
## 최성호
- 로그인, 로그아웃, 회원가입 구현
- Superuser 생성 오류 해결
- 프로필 페이지 수정중

## 오기선
- 전체 게시글 조회 페이지 처리 기능 추가
- 게시글 생성, 수정 추가
- 뒤로가기 추가

# 2023-11-21

## 김선욱
- 음악 플레이어 추가
- 날씨 데이터를 통한 랜덤 영화 추천 구현
- 영화 데이터 무한 루프 돌아가기 삭제
- 랙 제거를 위해 단순한 영화 카드 나열로 변경
- 영화 장르별 추천 구현

## 오기선
- 게시글 수정 삭제 기능 추가
- 게시글에서 유저 프로필 바로 가기 기능 추가
