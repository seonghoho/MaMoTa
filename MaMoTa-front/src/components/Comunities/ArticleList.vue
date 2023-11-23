<template>
  <div class="grid-container">
    <h1>게시물 리스트 뷰</h1>
    <RouterLink :to="{ name: 'articleCreate' }"> 게시글 생성</RouterLink>
    <div class="grid">
      <div
        v-if="productIsEmpty"
        v-for="article in paginatedArticles"
        :key="article.id"
        class="article_list"

      >
      <!-- @click="goDetail(article.id)" -->

        <!-- {{ article }} 객체확인용 -->
        <!-- <p>게시글 순서{{ article.id }} 관련 영화 제목{{ article.movie.title }}</p> -->
        <!-- <RouterLink  :to="`/user/profile/${article.user}`"
              class="router-link"
              >
              {{ article.username }}
            
            </RouterLink> 라우터링크로 유저 프로필가는 부분 구현 삭제예정 -->

        <p></p>
        <div @click.stop="goProfile(article.user)">
          {{ article.username }} 이 부분 누르면 유저 프로필로~
        </div>
        <p></p>
        <p>글쓴이가 준 평점 {{ article.rate }}</p>
        <p>게시글 생성일{{ article.created_at }}</p>
        <p>게시글 수정일{{ article.updated_at }}</p>
        <p>댓글 개수 {{ article.comment_count }} 끝에 배치 필요</p>

        <Like :article="article" />
        <p @click.stop="goLike(article.id)" class="blue">
          {{ article.like_users.includes(userStore.userData.pk)
            ? '좋아요 취소'
            : '좋아요' }}
        </p>
        <p>{{ article.like_users.length }}</p>
        <hr>
      </div>

      <div v-else>
        데이터 로딩 중...
      </div>
    </div>

    <!-- 로딩영역 추가 삭제예정-->
    <div>
      <button @click="prevPage" :disabled="currentPage == 1">이전</button>

      <span v-for="page in totalPages" :key="page">
        <button
          @click="goToPage(page)"
          :class="{ 'selected': currentPage === page }"
        >
          {{ page }}
        </button>
      </span>

      <button @click="nextPage" :disabled="currentPage == totalPages">다음</button>
    </div>
  </div>
</template>

<script setup>
import Like from '@/components/Comunities/Like.vue'
import { RouterLink } from 'vue-router'
import { ref, computed, onMounted } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/userStore'

const router = useRouter()
const store = useArticleStore()
const itemsPerRow = 3 // 한 줄에 표시할 아이템 수
const itemsPerPage = 9
const currentPage = ref(1)
const userStore = useUserStore()

onMounted(() => {
  store.getArticleList()
})

const goProfile = (userId) => {
  router.push({ name: 'userProfile', params: { userId: userId } })
}
// 상세페이지가기
const goDetail = (id) => {
  router.push({name:'detail', params:{id: id}})
}

const goLike = (articleId) => {
  store.likeArticle(articleId)
}

const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page
  }
}

const productIsEmpty = computed(() => {
  return paginatedArticles.value.length > 0 ? true : false
})

const paginatedArticles = computed(() => {
  if (!store.articleList.article) {
    return []
  }

  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage

  return store.articleList.article.slice(start, end)
})

const totalPages = computed(() => {
  if (!store.articleList.article) {
    return 0
  }

  return Math.ceil(store.articleList.article.length / itemsPerPage)
})

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value += 1
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value -= 1
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}
</script>

<style scoped>
.grid-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.article_list {
  color: white;
  width: 30%; /* 한 줄에 3개의 아이템이 표시되도록 조정 */
  margin-bottom: 16px; /* 각 아이템 아래 간격 조정 */
}

/* 선택된 페이지에 대한 스타일링 */
.selected {
  font-weight: bold;
  text-decoration: underline;
}

.blue {
  color: black;
  background-color: blue;
  width: 10%;
}
</style>
