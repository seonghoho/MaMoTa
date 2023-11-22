<!-- 댓글 나오는 컴포넌트 -->

<template>
  <li>
    <!-- {{ comment }}댓글 개체 확인 -->
    <!-- <p>{{ comment.article }}</p> -->

    <span class="comment-id"> {{ comment.username }}</span>
    <span class="comment-content">{{ comment.content }}</span>

    <div>
      <p>데이터 확인용~삭제예정</p>
      <p>{{ comment }}</p>
      <p>{{ comment.article }}</p>
      <p>{{ comment.id }}</p>
      <!-- <p>{{ authStore.userData.pk }}</p> -->
    </div>
    <button 
      v-if="comment.user === authStore.userData.pk"
      @click="store.commentDelete(comment.article, comment.id)"
    >
      🗑
    </button>
  </li>
</template>

<script setup>
import { useCommentStore } from '@/stores/comments';
import { useUserStore } from '@/stores/userStore';
const authStore = useUserStore()
const store = useCommentStore()

// const commentDelete = (a,b) => {
//   store.commentDelete(a,b)
// }



defineProps({
  comment: Object
})
</script>

<style lang="scss" scoped>

</style>