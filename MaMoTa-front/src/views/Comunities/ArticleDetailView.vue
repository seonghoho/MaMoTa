<!-- 데이터 상세 페이지 뷰 작성 -->

<template>
  <div>
    <h1>게시글 상세페이지에 온걸 환영해 ^^</h1>


  </div>

  <div v-if="store.detailArticle.data" class="post-details">
    <h1>게시글 상세 정보</h1>
    <div class="post-info">
      <p class="post-id">{{ store.detailArticle.data.id }} 번 글</p>
      <p class="post-title">글 제목:{{ store.detailArticle.data.title }}</p>
    </div>
    <hr>
    <div class="post-dates">
      <p class="created-date">작성일: {{ store.detailArticle.data.created_at }}</p>
      <p class="updated-date">수정일: {{ store.detailArticle.data.updated_at }}</p>
    </div>
    <hr>
    <p class="post-content">글 내용:{{ store.detailArticle.data.content }}</p>
    <!-- <CommentCreate 
      :postPk="store.detailPost.id"
    /> -->
    <ul class="comment-list">
      <CommentList
        v-for="comment in store.detailArticle.data.comment_set"
        :key="comment.id"
        class="comment-item"
        :comment="comment"
      />
    </ul> 

    <!-- 댓글 작성 및 댓글 출력 부분 추가 예정 -->

    <hr>
  </div>
</template>

<script setup>
// import CommentCreate from '../components/CommentCreate.vue';
import CommentList from '@/components/Comunities/CommentList.vue';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useArticleStore } from '@/stores/article';

const route = useRoute()
const store = useArticleStore()






// 데이터연결
onMounted(() => {
  console.log(store.detailArticle.data)
  console.log(route.params.id)
  store.getDetailArticle(route.params.id)
})



</script>

<style lang="scss" scoped>
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