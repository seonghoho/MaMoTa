<template>
  <div class="grid-container">
    <h1> </h1>
    <!-- <RouterLink :to="{ name: 'articleCreate' }"> 게시글 생성</RouterLink> -->
    <button @click="navigateToArticleCreate" class="create_button">게시글 생성</button>

    <div class="grid">
      <div
        v-if="productIsEmpty"
        v-for="article in paginatedArticles"
        :key="article.id"
        class="article_list"
      >
        <!-- 게시글 내용 출력 부분 -->
        <!-- <h3>{{ article.title }}</h3> -->
        <!-- 내용이 길 경우에 대비하여 일부만 출력하거나 스타일을 조절할 수 있습니다. -->

        <Like :article="article" />
        <div class="like-button">
          <font-awesome-icon
            @click.stop="goLike(article.id)"
            :icon="['fas', 'thumbs-up']"
            beat
            size="2xl"
            v-if="!article.like_users.includes(userStore.userData.pk)"
          />
          <font-awesome-icon
            @click.stop="goLike(article.id)"
            :icon="['fas', 'heart']"
            bounce
            size="2xl"
            style="color: #ff1900;"
            v-else
          />
        </div>

        <h3 class="like-count">{{ article.like_users.length }}</h3>
        <hr>
      </div>

      <div v-else>
        데이터 로딩 중...
      </div>
    </div>

    <div>
      <!-- 페이지 이동 버튼 -->
      <button @click="prevPage" :disabled="currentPage === 1">이전</button>

      <span v-for="page in totalPages" :key="page">
        <button
          @click="goToPage(page)"
          :class="{ 'selected': currentPage === page }"
        >
          {{ page }}
        </button>
      </span>

      <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
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

const navigateToArticleCreate = () => {
  router.push({ name: 'articleCreate' });
};


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
.create_button {
  width: 340px;
  height: 40px;
  margin: 20px;
  border-radius: 5px;
  box-shadow: 0 0 0 5px rgba(255, 255, 255, 0.2);
  background-color: #d3ffea ;

}
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
  width: calc(33.33% - 16px); /* 한 줄에 3개의 아이템이 표시되도록 조정 */
  margin-bottom: 16px;
  min-height: 150px;
  box-sizing: border-box;
}

.selected {
  font-weight: bold;
  text-decoration: underline;
}

.like-button {
  margin-top: 25px;
}

.like-count {
  margin-top: 5px;
  margin-left: 15px;
}
</style>
