<!-- 댓글 나오는 컴포넌트 -->

<template>
  <li>
    <h3>야 댓글좀</h3>
    <!-- {{ comment }} -->

    <span class="comment-id">{{ comment.id }} {{ comment.username }}</span>
    <span class="comment-content">{{ comment.content }}</span>
  </li>
</template>

<script setup>
defineProps({
  comment: Object
})
</script>

<style lang="scss" scoped>

</style>