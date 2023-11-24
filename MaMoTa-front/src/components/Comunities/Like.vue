
<template>
  <div class="card" :data-state="currentState">
    <div class="card-header">
      <div class="card-cover" :style="{ backgroundImage: `url('${coverImageUrl}')` }"></div>

      <img class="card-avatar" :src="avatarImageUrl" alt="avatar" />

      <h1 class="card-feel" v-if="article.rate===1"> 별로에요!</h1>
      <h1 class="card-feel" v-if="article.rate===2"> 조금아쉬워요..</h1>
      <h1 class="card-feel" v-if="article.rate===3"> 보통이에요</h1>
      <h1 class="card-feel" v-if="article.rate===4"> 추천해요ㅎㅎ</h1>
      <h1 class="card-feel" v-if="article.rate===5"> 완전 재밌어요!</h1>


      <!-- <h1 class="card-fullname">{{ fullName }}</h1> -->
      <h2 class="card-jobtitle" v-if="article.rate===1">화가난다..!</h2>
      <h2 class="card-jobtitle" v-if="article.rate===2">재밌는거 없나?</h2>
      <h2 class="card-jobtitle" v-if="article.rate===3">이 정도면 괜찮아</h2>
      <h2 class="card-jobtitle" v-if="article.rate===4">혼자 보기 아까워</h2>
      <h2 class="card-jobtitle" v-if="article.rate===5">꼭 보세요 다들..!</h2>
    </div>
    <div class="card-main">
      <div class="card-section" :class="{ 'is-active': currentState === 'about' }">
        <div class="card-content">

          <div class="card-subtitle">영화</div>
          <p>{{ article.movie_title }}</p>

          <p></p>
          <!-- <p>{{ article.title }}</p> -->
          <div class="card-subtitle">평점</div>
          <p class="card-desc">
          <div class="star-rating">
            <template v-for="n in Math.floor(article.rate)">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polygon
                  points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
              </svg>
            </template>
            <template v-if="article.rate % 1 !== 0">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polygon
                  points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
              </svg>
            </template>
          </div>
          </p>
          <p></p>
          <div class="card-subtitle">리뷰</div>
          <p></p>

          <div>
            {{ article.content.slice(0, 80) }}
            <span v-if="article.content.length > 80">....</span>
          </div>
          <div> </div>
          <RouterLink :to="{ name: 'detail', params: { id: article.id } }" class="btn btn-light btn-sm mt-2" style="background-color: #d3ffea; border: 2px solid gray;">
            상세 보기
          </RouterLink>
        </div>
        <div class="card-social">
          <a href="#"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M15.997 3.985h2.191V.169C17.81.117 16.51 0 14.996 0c-3.159 0-5.323 1.987-5.323 5.639V9H6.187v4.266h3.486V24h4.274V13.267h3.345l.531-4.266h-3.877V6.062c.001-1.233.333-2.077 2.051-2.077z" />
            </svg></a>
          <!-- 나머지 소셜 미디어 아이콘 추가 -->
        </div>
      </div>
      <div class="card-section" :class="{ 'is-active': currentState === 'experience' }">
        <div class="card-content">
          <div class="card-subtitle">경력</div>
          <div class="card-timeline">
            <!-- 경력 항목 추가 -->
          </div>
        </div>
      </div>
      <div class="card-section" :class="{ 'is-active': currentState === 'contact' }">
        <div class="card-content">
          <div class="card-subtitle">작성자</div>
          <p>{{ article.username }}</p>
          <div class="card-subtitle">작성일</div>
          <p>{{ formatDateTime(article.created_at).slice(0,12) }}</p>
          <p>{{ formatDateTime(article.created_at).slice(14,28) }}</p>

          <div class="card-subtitle">수정일</div>
          <p>{{ formatDateTime(article.updated_at).slice(0,12) }}</p>
          <p>{{ formatDateTime(article.updated_at).slice(14,28) }}</p>
          <!-- <p>{{ article.user }}</p> -->
          <!-- <RouterLink :to="{ name: 'userProfile', params: { id: article.user } }" class="btn btn-light btn-sm mt-1">
            프로필
          </RouterLink> -->
          <div @click="goProfile(article.user)" class="btn btn-light btn-sm mt-1" style="background-color: #d3ffea; border: 2px solid gray;"> 프로필</div>

        </div>
      </div>
    </div>
    <div class="card-buttons">
      <button @click="changeSection('about')" :class="{ 'is-active': currentState === 'about' }">영화리뷰</button>
      <button>
        <RouterLink :to="{ name: 'search', query: { movieTitle: article.movie_title } }" class="router-link">
           영화정보
        </RouterLink>
      </button>
      <button @click="changeSection('contact')" :class="{ 'is-active': currentState === 'contact' }">유저정보</button>
    </div>
  </div>
</template>

<script setup>

import { useRouter,RouterLink } from 'vue-router';
import { computed } from '@vue/reactivity';
import { useUserStore } from '@/stores/userStore';
import { useArticleStore } from '@/stores/article';
import { ref } from 'vue';

const router = useRouter()


const store = useArticleStore()
const userStore = useUserStore()
// const likeEmpty = ref(false);

const goProfile = (userId) => {
  console.log(userId)
  router.push({ name: 'userProfile', params: { userId: userId } })
}

const { article } = defineProps(['article'])
// 좋아요 클릭함수
const goLike = (articleId) => {
  store.likeArticle(articleId)
}
// console.log(userStore.userData.pk)
console.log(article.like_users)

const likeEmpty = computed(() => {
  return article.like_users.length > 0 && article.like_users.includes(userStore.userData.pk) ? true : false
})


// 시간 출력 형식 수정
const formatDateTime = (dateTimeString) => {
  const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    timeZoneName: 'short'
  };

  const formattedDateTime = new Date(dateTimeString).toLocaleString('ko-KR', options);
  return formattedDateTime;
};


const currentState = ref('about'); // 초기 섹션 설정
const coverImageUrl = `/src/assets/Images/rateemoji/back_emoji_${article.rate}.png`;
// const avatarImageUrl = 'https://images.unsplash.com/photo-1549068106-b024baf5062d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80';
const avatarImageUrl = `/src/assets/Images/rateemoji/emoji_${article.rate}.png`
const fullName = 'William Rocheald';

const changeSection = (section) => {
  currentState.value = section;
};


</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=DM+Sans:400,500|Jost:400,500,600&display=swap");

* {
  box-sizing: border-box;
}

body {
  color: #2b2c48;
  font-family: "Jost", sans-serif;
  background-image: url(https://images.unsplash.com/photo-1566738780863-f9608f88f3a9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2378&q=80);

  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
  padding: 20px;
}

.card {
  max-width: 340px;
  /* height: 570px; */
  margin: auto;
  overflow-y: auto;
  position: relative;
  z-index: 1;
  overflow-x: hidden;
  background-color: rgba(255, 255, 255, 1);
  display: flex;
  transition: 0.3s;
  flex-direction: column;
  border-radius: 10px;
  box-shadow: 0 0 0 8px rgba(255, 255, 255, 0.2);
  background-color: #d3ffea;
}

.card[data-state="#about"] {
  height: 450px;
  }
  .card[data-state="#about"] .card-main {
    padding-top: 0;

}

.card[data-state="#contact"] {
  height: 430px;
}

.card[data-state="#experience"] {
  height: 550px;
}

.card .is-active {
  .card-header {
    height: 80px;
  }

  .card-cover {
    height: 100px;
    top: -50px;
  }

  .card-avatar {
    transform: none;
    left: 20px;
    width: 50px;
    height: 50px;
    bottom: 10px;
  }

  .card-fullname,
  .card-jobtitle {
    left: 86px;
    transform: none;
  }

  .card-fullname {
    bottom: 18px;
    font-size: 19px;
  }

  .card-jobtitle {
    bottom: 16px;
    letter-spacing: 1px;
    font-size: 10px;
  }
}

.card-header {
  position: relative;
  display: flex;
  height: 200px;
  flex-shrink: 0;
  width: 100%;
  transition: 0.3s;

  * {
    transition: 0.3s;
  }
}

.card-cover {
  width: 100%;
  height: 100%;
  position: absolute;
  height: 160px;
  top: -20%;
  left: 0;
  will-change: top;
  background-size: cover;
  background-position: center;
  filter: blur(30px);
  transform: scale(1.2);
  transition: 0.5s;
}

.card-avatar {
  width: 100px;
  height: 100px;
  box-shadow: 0 8px 8px rgba(0, 0, 0, 0.2);
  border-radius: 50%;
  object-position: center;
  object-fit: cover;
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  animation: bounce 0.5s infinite alternate;
  margin-bottom: 50px;
}

@keyframes bounce {
  100% {
    transform: translateY(0) translateX(-50%);
  }
  0% {
    transform: translateY(-20px) translateX(-50%);
  }
}


.card-feel {
  position: absolute;
  bottom: 0;
  font-size: 22px;
  font-weight: 700;
  text-align: center;
  white-space: nowrap;
  transform: translateY(-10px) translateX(-50%);
  left: 50%;
}


.card-jobtitle {
  position: absolute;
  bottom: 0;
  font-size: 11px;
  white-space: nowrap;
  font-weight: 500;
  opacity: 0.7;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin: 0;
  left: 50%;
  transform: translateX(-50%) translateY(-7px);
}

.card-main {
  position: relative;
  flex: 1;
  display: flex;
  padding-top: 10px;
  flex-direction: column;
}

.card-subtitle {
  font-weight: 700;
  font-size: 13px;
  margin-bottom: 8px;
}

.card-content {
  padding: 20px;
}

.card-desc {
  line-height: 1.6;
  color: #636b6f;
  font-size: 14px;
  margin: 0;
  font-weight: 400;
  font-family: "DM Sans", sans-serif;
}

.router-link {
  text-decoration: none;
  color: black;
}

.card-social {
  display: flex;
  align-items: center;
  padding: 0 20px;
  margin-bottom: 30px;

  svg {
    fill: rgb(165, 181, 206);
    width: 16px;
    display: block;
    transition: 0.3s;
  }

  a {
    color: #8797a1;
    height: 32px;
    width: 32px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    transition: 0.3s;
    background-color: rgba(93, 133, 193, 0.05);
    border-radius: 50%;
    margin-right: 10px;

    &:hover {
      svg {
        fill: darken(rgb(165, 181, 206), 20%);
      }
    }

    &:last-child {
      margin-right: 0;
    }
  }
}

.card-buttons {
  display: flex;
  margin-top: auto;
  position: sticky;
  bottom: 0;
  left: 0;
  text-align: center;
  background-color: #d3ffea;
  
}
.card-buttons button {
    flex: 1 1 auto;
    user-select: none;
    background: 0;
    font-size: 14px;
    border: 0;
    padding: 15px 5px;
    cursor: pointer;
    color: #5c5c6d;
    transition: 0.3s;
    /* font-family: "Jost", sans-serif; */
    outline: 0;
    border-bottom: 3px solid transparent;
    background-color: #d3ffea;
    font-weight: 400;
}
.card-buttons .is-active,
.card-buttons :hover {
      color: #2b2c48;
      border-bottom: 10px solid #938dff;
      background: linear-gradient(to bottom,
          rgba(127, 199, 231, 0) 0%,
          rgba(200, 196, 255, 0.2) 44%,
          rgba(164, 107, 255, 0.4) 100%);
    
  
}

.card-section {
  display: none;

  &.is-active {
    display: block;
    animation: fadeIn 0.6s both;
  }
}

@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translatey(40px);
  }

  100% {
    opacity: 1;
  }
}

.card-timeline {
  margin-top: 30px;
  position: relative;

  &:after {
    background: linear-gradient(to top,
        rgba(134, 214, 243, 0) 0%,
        rgba(81, 106, 204, 1) 100%);
    content: "";
    left: 42px;
    width: 2px;
    top: 0;
    height: 100%;
    position: absolute;
    content: "";
  }
}

.card-item {
  position: relative;
  padding-left: 60px;
  padding-right: 20px;
  padding-bottom: 30px;
  z-index: 1;

  &:last-child {
    padding-bottom: 5px;
  }

  &:after {
    content: attr(data-year);
    width: 10px;
    position: absolute;
    top: 0;
    left: 37px;
    width: 8px;
    height: 8px;
    line-height: 0.6;
    border: 2px solid #fff;
    font-size: 11px;
    text-indent: -35px;
    border-radius: 50%;
    color: rgba(#868686, 0.7);
    background: linear-gradient(to bottom,
        lighten(#516acc, 20%) 0%,
        #516acc 100%);
  }
}

.card-item-title {
  font-weight: 500;
  font-size: 14px;
  margin-bottom: 5px;
}

.card-item-desc {
  font-size: 13px;
  color: #6f6f7b;
  line-height: 1.5;
  font-family: "DM Sans", sans-serif;
}

.card-contact-wrapper {
  margin-top: 20px;
}

.card-contact {
  display: flex;
  align-items: center;
  font-size: 13px;
  color: #6f6f7b;
  font-family: "DM Sans", sans-serif;
  line-height: 1.6;
  cursor: pointer;

  &+& {
    margin-top: 16px;
  }

  svg {
    flex-shrink: 0;
    width: 30px;
    min-height: 34px;
    margin-right: 12px;
    transition: 0.3s;
    padding-right: 12px;
    border-right: 1px solid #dfe2ec;
  }
}

.contact-me {
  border: 0;
  outline: none;
  background: linear-gradient(to right,
      rgba(83, 200, 239, 0.8) 0%,
      rgba(81, 106, 204, 0.8) 96%);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
  color: #fff;
  padding: 12px 16px;
  width: 100%;
  border-radius: 5px;
  margin-top: 25px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  font-family: "Jost", sans-serif;
  transition: 0.3s;
}



.star-rating {
  display: flex;
  color: #f8ce0b;
  /* 별 색상 지정, 원하는 색상으로 변경 가능 */
}

.star-rating svg {
  width: 20px;
  height: 20px;
  fill: currentColor;
  margin-right: 2px;
  /* 별 간격 조정 */
}
</style>

