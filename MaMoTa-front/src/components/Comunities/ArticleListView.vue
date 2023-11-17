<!-- 게시글 전체페이지 조회뷰 -->

<template>


  <div>
    <h1>게시물 리스트 뷰</h1>
    <h2>게시글 생성 링크작성 예정</h2>
    <ul>
      <div
      v-for="article in store.articleList.article"
      :key="article.id"
      @click="goDetail(article.id)"
      >
      <p>게시글 순서{{ article.id }} 관련 영화 제목{{ article.movie.title }}</p>
      <p>글쓴이 아이디 {{ article.username }}  뒤에 이메일 필터링 예정</p>
      <p>글쓴이가 준 평점 {{ article.rate }}</p>
      <p>게시글 생성일{{ article.created_at }}</p>
      <p>게시글 수정일{{ article.updated_at }}</p>
        <hr>
      </div>
      <!-- <h5>{{ store.articleList }}</h5> -->
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/article';
import { useRouter } from 'vue-router'
const router = useRouter()
const store = useArticleStore()

// 바로 아티클 리스트 데이터받기
onMounted(() => {
  store.getArticleList()
})


const goDetail = (id) => {
  router.push({name:'detail', params:{id: id}})
}
</script>

<style scoped>

</style>