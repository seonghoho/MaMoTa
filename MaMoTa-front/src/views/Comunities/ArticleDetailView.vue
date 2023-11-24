<!-- 데이터 상세 페이지 뷰 작성 -->

<template>
  <div class="box"></div>

  <div class="card" :data-state="currentState" v-if="a">
      <div class="card-header">
        <div class="card-cover" :style="{ backgroundImage: `url(/src/assets/Images/rateemoji/back_emoji_${store.detailArticle.data.rate}.png)` }"></div>
  

        <img class="card-avatar" :src=" `/src/assets/Images/rateemoji/emoji_${store.detailArticle.data.rate}.png`  " alt="avatar" />
  
        <h1 class="card-feel" v-if="store.detailArticle.data.rate===1"> 별로에요!</h1>
        <h1 class="card-feel" v-if="store.detailArticle.data.rate===2"> 조금아쉬워요..</h1>
        <h1 class="card-feel" v-if="store.detailArticle.data.rate===3"> 보통이에요</h1>
        <h1 class="card-feel" v-if="store.detailArticle.data.rate===4"> 추천해요ㅎㅎ</h1>
        <h1 class="card-feel" v-if="store.detailArticle.data.rate===5"> 완전 재밌어요!</h1>
      </div>
    </div>


  <div v-if="store.detailArticle.data" class="post-details" :style="{ backgroundImage: `url(/src/assets/Images/rateemoji/back_emoji_${store.detailArticle.data.rate}.png)` }">
    <p></p>
    <!-- <h1>게시글 상세 정보</h1> -->
    <router-link :to="{ name: 'community' }" class="back-button btn btn-outline-dark btn-sm" style="font-weight: bolder; border-width: 2px;" >뒤로 가기</router-link>
    <div class="post-info">

      <!-- <p class="post-id">{{ store.detailArticle.data.id }} 번 글</p> -->
      <p class="post-title">영화 제목: {{ store.detailArticle.data.movie_title }}</p>
      <RouterLink :to="{ name: 'search', query: { movieTitle: store.detailArticle.data.movie_title } }" class="back-button btn btn-outline-dark btn-sm" style="font-weight: bolder; border-width: 2px;" >영화 정보 보기</RouterLink>
      <p class="post-title">제목:{{ store.detailArticle.data.title }}</p>
    </div>
    <div @click.stop="goProfile(store.detailArticle.data.user)">
      작성자:{{ store.detailArticle.data.username }}
    </div>
    <!-- <hr> -->
    <!-- <div class="post-dates">
      <p class="created-date">작성일: {{ store.detailArticle.data.created_at }}</p>
      <p class="updated-date">수정일: {{ store.detailArticle.data.updated_at }}</p>
    </div> -->
    <!-- <hr> -->
    <p class="post-content">리뷰:{{ store.detailArticle.data.content }}</p>

    <p>좋아요 개수 {{ store.detailArticle.data.like_users.length }}</p>


    

    <span
      v-if="store.detailArticle.data.user === authStore.userData.pk"
    >
      <button @click="router.push({name:'articleUpdate', params:{pk:store.detailArticle.data.id}})">게시글수정</button>
      <button @click="store.deleteArticle(store.detailArticle.data.id)">🗑</button>
      <!-- <p>{{ store.detailArticle.data.id }}</p> -->
    </span>
    
    <!-- <댓글작성부분 추가 삭제 내용 포함> -->
    <CommentCreate 
      :articlePk="store.detailArticle.data.id"
    />
    <ul class="comment-list">
      <CommentList
        v-for="comment in store.detailArticle.data.comment_set"
        :key="comment.id"
        class="comment-item"
        :comment="comment"

      />
    </ul> 


    <hr>
  </div>
</template>

<script setup>
import CommentCreate from '@/components/Comunities/CommentCreate.vue';
import CommentList from '@/components/Comunities/CommentList.vue';
import { onMounted,ref } from 'vue';
import { useRoute,useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/article';
import { useUserStore } from '@/stores/userStore'
import { useMovieStore } from '@/stores/movie';
import { computed } from '@vue/reactivity';
const authStore = useUserStore()


const route = useRoute()
const store = useArticleStore()
const router = useRouter()
// 수정 및 삭제 태그 추가 부분


//이미지
const currentState = ref('about'); // 초기 섹션 설정
  // const avatarImageUrl = 'https://images.unsplash.com/photo-1549068106-b024baf5062d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80';



  
// 데이터연결
onMounted(() => {
  // console.log(store.detailArticle.data)
  // console.log(route.params.id)
  store.getDetailArticle(route.params.id)

})

const a = computed(() => {
  return store.detailArticle.data && store.detailArticle.data.rate > 0 ? true : false
});



// if (a.value === true) {
//     coverImageUrl = `/src/assets/Images/rateemoji/back_emoji_${store.detailArticle.data.rate}.png`;
//     avatarImageUrl = `/src/assets/Images/rateemoji/emoji_${store.detailArticle.data.rate}.png`;
//   }

// 프로필 가는 부분
const goProfile = (userId) => {
  router.push({name:'userProfile', params:{userId: userId}})
}

</script>

<style lang="scss" scoped>
.box {
  height: 100px;
}
.card {
  width: 60%;
  margin: auto;
}
.post-details {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;

  overflow-y: auto;
  position: relative;
  z-index: 1;
  overflow-x: hidden;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 1);


}

.post-info {
  margin-bottom: 20px;
}

.category {
  font-size: 16px;
  color: #333;
}

.post-id {
  font-size: 14px;
  color: #888;
}

.post-title {
  font-size: 24px;
  font-weight: bold;
  margin-top: 10px;
  margin-bottom: 20px;
}

.post-dates {
  font-size: 12px;
  color: #888;
  margin-bottom: 10px;
}

.post-content {
  font-size: 16px;
  line-height: 1.6;
  margin-bottom: 20px;
}

.comment-list {
  list-style: none;
  padding: 0;
}

.comment-item {
  font-size: 14px;
  margin-bottom: 10px;
}

.comment-id {
  font-weight: bold;
  margin-right: 5px;
}

.comment-content {
  margin-left: 5px;
}

.card {
    max-width: 600px;
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
    // box-shadow: 0 0 0 8px rgba(255, 255, 255, 0.2);
  }
  
  .card[data-state="#about"] {
    height: 450px;
  
    .card-main {
      padding-top: 0;
    }
  }
  
  .card[data-state="#contact"] {
    height: 430px;
  }
  
  .card[data-state="#experience"] {
    height: 550px;
  }
  
  .card.is-active {
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
    transform: translateX(-50%) translateY(-64px);
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
    background-color: #fff;
    margin-top: auto;
    position: sticky;
    bottom: 0;
    left: 0;
  
    button {
      flex: 1 1 auto;
      user-select: none;
      background: 0;
      font-size: 13px;
      border: 0;
      padding: 15px 5px;
      cursor: pointer;
      color: #5c5c6d;
      transition: 0.3s;
      font-family: "Jost", sans-serif;
      font-weight: 500;
      outline: 0;
      border-bottom: 3px solid transparent;
  
      &.is-active,
      &:hover {
        color: #2b2c48;
        border-bottom: 3px solid #8a84ff;
        background: linear-gradient(to bottom,
            rgba(127, 199, 231, 0) 0%,
            rgba(207, 204, 255, 0.2) 44%,
            rgba(211, 226, 255, 0.4) 100%);
      }
    }
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