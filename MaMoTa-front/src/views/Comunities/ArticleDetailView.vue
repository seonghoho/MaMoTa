<!-- 데이터 상세 페이지 뷰 작성 -->

<template>
  <div>
    <h1>게시글 상세페이지에 온걸 환영해 ^^</h1>

  </div>

  <div v-if="store.detailArticle.data" class="post-details">
    <h1>게시글 상세 정보</h1>
    <router-link :to="{ name: 'community' }" class="back-button btn btn-primary">뒤로 가기</router-link>
    <div class="post-info">
      <p class="post-id">{{ store.detailArticle.data.id }} 번 글</p>
      <p class="post-title">영화 제목: {{ store.detailArticle.data.movie_title }}</p>
      <RouterLink :to="{ name: 'search', query: { movieTitle: store.detailArticle.data.movie_title } }" class="btn btn-primary">영화 정보 보기</RouterLink>
      <p class="post-title">글 제목:{{ store.detailArticle.data.title }}</p>
    </div>
    <div @click.stop="goProfile(store.detailArticle.data.user)">
      작성자:{{ store.detailArticle.data.username }} 누르면 프로필 들어감
    </div>
    <hr>
    <div class="post-dates">
      <p class="created-date">작성일: {{ store.detailArticle.data.created_at }}</p>
      <p class="updated-date">수정일: {{ store.detailArticle.data.updated_at }}</p>
    </div>
    <hr>
    <p class="post-content">글 내용:{{ store.detailArticle.data.content }}</p>

    <p>좋아요 개수 {{ store.detailArticle.data.like_users.length }}</p>

    <!-- <p>댓글 개수 {{ store.detailArticle.data.comment_set }}</p> -->
    
    <!-- <p>{{ store.detailArticle.data.user }}</p>
    <p>{{ authStore }}</p> pk확인부분! 확인용 -->
    <span
      v-if="store.detailArticle.data.user === authStore.userData.pk"
    >
      <!-- <p>여기야여기야!</p> -->
      <button @click="router.push({name:'articleUpdate', params:{pk:store.detailArticle.data.id}})">수정</button>
      <button @click="store.deleteArticle(store.detailArticle.data.id)">🗑</button>
      <p>{{ store.detailArticle.data.id }}</p>
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
import ArticleMovieCard from '@/components/Movies/ArticleMovieCard.vue'
import { onMounted } from 'vue';
import { useRoute,useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/article';
import { useUserStore } from '@/stores/userStore'
import { useMovieStore } from '@/stores/movie';
const authStore = useUserStore()

const route = useRoute()
const store = useArticleStore()
const router = useRouter()
// 수정 및 삭제 태그 추가 부분


// 데이터연결
onMounted(() => {
  // console.log(store.detailArticle.data)
  // console.log(route.params.id)
  store.getDetailArticle(route.params.id)
})


// 프로필 가는 부분
const goProfile = (userId) => {
  router.push({name:'userProfile', params:{userId: userId}})
}

</script>

<style lang="scss" scoped>
.card {
  width: 60%;
  margin: auto;
}
.post-details {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  background-color: #fff;
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
</style>