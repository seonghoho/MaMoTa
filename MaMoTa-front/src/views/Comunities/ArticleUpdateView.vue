
<template>
    <div class="create-article-page">
      <h1>게시글 수정 페이지</h1>
      <form @submit.prevent="updateArticle" class="article-form">
      <router-link :to="{ name: 'community' }" class="back-button">게시글 목록</router-link>
        <label for="title" class="form-label">글 제목:</label>
        <input type="text" name="title" v-model="title" class="form-input">
        <label for="rate" class="form-label">평점 선택:</label>
        <select name="rate" id="rate" v-model="rate" class="form-select">
          <option v-for="i in 10" :key="i/2" :value="(i/2).toFixed(1)">
          {{ (i/2).toFixed(1) }}
          </option>
        </select>
  
        <label for="movie" class="form-label">영화:</label>
        <input type="text" name="movie" v-model="movie" class="form-input">
  
  
        <label for="content" class="form-label">내용:</label>
        <textarea name="content" id="content" cols="30" rows="10" v-model="content" class="form-textarea"></textarea>
  
        <button class="submit-button">게시글 생성</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useArticleStore } from '@/stores/article'
  import { useRouter,useRoute } from 'vue-router';
  const router = useRouter()
  const title = ref('')
  const content = ref('')
  // const category = ref(1)
  const route = useRoute()

  const rate = ref('')
  const movie = ref('')
  const articleStore = useArticleStore()
  // const categoryStore = useCategoryStore()
  
  // onMounted(() => {
  //   categoryStore.getCategoryList()
  // })
  // 글 수정 후 다시 커뮤니티로 
  const updateArticle = function () {
    const article = {
        pk:route.params.id,
      title: title.value,
      content: content.value,
      rate: rate.value,
      movie: movie.value
    }
    articleStore.updateArticle(article)
    router.push({name: 'detail', params:{id:route.params.id}})
  }
  </script>
  
  <style scoped>
  .create-article-page {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    color: violet;
    margin-top: 80px;
  }
  
  h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }
  
  .article-form {
    background-color: rgba(79, 50, 103, 0.6);
  /* border: 1px solid #ccc; */
    border-radius: 20px;
    padding: 20px;
  }
  
  .form-label {
    font-size: 16px;
    display: block;
    margin-bottom: 8px;
  }
  
  .form-select,
  .form-input,
  .form-textarea {
    width: 100%;
    padding: 10px;
    font-size: 14px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 10px;
    background-color: #bba6fa;

  }
  
  .submit-button {
    display: block;
    width: 100%;
    padding: 8px;
    font-size: 20px;
    font-weight: bolder;
    background-color: #E384FF;
    color: #865DFF;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.2s;
  }
  
  .submit-button:hover {
    background-color: #0056b3;
  }
  </style>
  