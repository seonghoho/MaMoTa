<template>


  <div >
    <h1>게시물 리스트 뷰</h1>
    <RouterLink :to="{name:'articleCreate'}"> 게시글 생성</RouterLink>
    <ul>
      <div
      v-if="productIsEmpty"
      v-for="article in paginatedArticles"
      :key="article.id"
      @click="goDetail(article.id)"
      class="article_list"
      >
      <!-- {{ article }} -->
      <p>게시글 순서{{ article.id }} 관련 영화 제목{{ article.movie.title }}</p>
      <p>글쓴이 아이디 {{ article.username }}  뒤에 이메일 필터링 예정</p>
      <p>글쓴이가 준 평점 {{ article.rate }}</p>
      <p>게시글 생성일{{ article.created_at }}</p>
      <p>게시글 수정일{{ article.updated_at }}</p>
      <p>댓글 개수 {{ article.comment_count }} 끝에 배치 필요</p>
      <P>좋아요 개수</P>
      <p>{{ article }} 객체 확인부분</p>
      <p>조회수 : {{ article.view_count }}</p>
        <hr>
      </div>
      <div v-else>
        데이터 로딩 중...
      </div>
      <!-- <h5>{{ store.articleList }}  객체 확인용</h5> -->
    </ul>

<!-- 페이지 로딩영역 -->
    <!-- <div>
      <button @click="prevPage" :disabled="currentPage == 1">이전</button>
      <span>{{ currentPage }} / {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage == totalPages">다음</button>
    </div> -->

  <!-- 로딩영역 추가 -->
  <div>
      <button @click="prevPage" :disabled="currentPage == 1">이전</button>
      
      <!-- 페이지 번호 클릭 이벤트 핸들러 추가 -->
      <span v-for="page in totalPages" :key="page">
        <button @click="goToPage(page)" :class="{ 'selected': currentPage === page }">{{ page }}</button>
      </span>
      
      <button @click="nextPage" :disabled="currentPage == totalPages">다음</button>
    </div>
  </div>
</template>

<script setup>

import { RouterLink } from 'vue-router'
import { ref,computed,onMounted } from 'vue';
import { useArticleStore } from '@/stores/article';
import { useRouter } from 'vue-router'
const router = useRouter()
const store = useArticleStore()
const itemsPerPage = 10;
const currentPage = ref(1);
// 바로 아티클 리스트 데이터받기

const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};


onMounted(() => {
  console.log(1)
  store.getArticleList()
  console.log(store)
})

const productIsEmpty = computed(() => {
  return paginatedArticles.value.length > 0 ? true : false
})


const goDetail = (id) => {
  router.push({name:'detail', params:{id: id}})
}

const paginatedArticles = computed(() => {
  if (!store.articleList.article) {
    console.log(2)
    return [];
  }
  console.log(3)

  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;

  return store.articleList.article.slice(start, end);
});

const totalPages = computed(() => {
  if (!store.articleList.article) {
    console.log(4)

    return 0;
  }
  console.log(5)

  return Math.ceil(store.articleList.article.length / itemsPerPage);
});

console.log(totalPages)
console.log(paginatedArticles)


const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value += 1;
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value -= 1;
  }
};
</script>

<style scoped>
.article_list {
  color: white;
}
/* 선택된 페이지에 대한 스타일링 */
.selected {
  font-weight: bold;
  text-decoration: underline;
}
</style>