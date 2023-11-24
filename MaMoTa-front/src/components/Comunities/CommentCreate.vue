<!-- 댓글생성 컴포넌트 제작 -->

<template>
  <form @submit.prevent="createComment">
    <label for="content">내용 : </label>
    <input type="text" class="transparent-input mt-1" name="content" id="content" style="border: 2px solid black; border-radius: 3px; " placeholder="댓글을 입력하세요." v-model="content">
    <button class="back-button btn btn-outline-dark btn-sm ms-1" style="font-weight: bolder; border-width: 2px; ">댓글 작성</button>
  </form>
</template>

<script setup>
import { useCommentStore } from '@/stores/comments.js'
import { ref } from 'vue';
const store = useCommentStore()
const props = defineProps({
  articlePk: Number
})
const content = ref('')
const createComment = function () {
  console.log(props)
  store.commentCreate(props.articlePk, content.value)
  content.value = ''
}
</script>

<style scoped>

.transparent-input {
  background-color: transparent;
  border: 1px solid #ced4da; /* 선택적으로 테두리 추가 */
}
</style>