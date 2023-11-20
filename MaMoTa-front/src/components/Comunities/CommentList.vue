<!-- 댓글 나오는 컴포넌트 -->

<template>
  <li>
    <h3>야 댓글좀</h3>
    <!-- {{ comment }}댓글 개체 확인 -->
    <!-- <p>{{ comment.article }}</p> -->

    <span class="comment-id">{{ comment.id }} {{ comment.username }}</span>
    <span class="comment-content">{{ comment.content }}</span>

    
    <!--댓글 삭제부분<button 
      v-if="comment.user.username === authStore.user.username"
      @click="commentDelete"
    >
      🗑
    </button> -->
  </li>
</template>

<script setup>
// import { useCommentStore } from '@/stores/comments';
// import { useAuthStore } from '@/stores/auth';
// const authStore = useAuthStore()
// const store = useCommentStore()

// const commentDelete = () => {
//   store.commentDelete(comment.article, comment.id)
// }



defineProps({
  comment: Object
})
</script>

<style lang="scss" scoped>

</style>