<template>
  <div class="card h-100 border-dark">
    <RouterLink
      :to="{name:'detail', params:{id: article.id}}"
    > 
    <div class="card-header">
      <img class="card-avatar" :src="`/src/assets/Images/rateemoji/emoji_${article.rate}.png`" alt="avatar" />
    </div>
      <div class="card-body">
        <h5 class="card-title">{{ article.title }}</h5>
        <div class="card-content">
          <div>{{ formatContent(article.content) }}</div>
          <div>{{ article.rate }} / 5</div>
        </div>
      </div>
    </RouterLink>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  article: Object
})


// const getFormattedTitle = computed(() => {
//   const title = props.article.movie.title || props.article.movie.name
//   return title.length > 15 ? title.slice(0, 15) + '...' : title
// })

// const avatarImageUrl = `/src/assets/Images/rateemoji/emoji_${article.rate}.png`

const formatContent = (content) => {
  const cont = content.length > 10 ? content.slice(0, 10) + '...' : content
  return cont.replace(/\n/g, '<br />')
}
</script>

<style scoped>
.card {
  min-width: calc(50% - 10px); /* 10px은 카드 사이의 간격으로 조절 가능 */
  height: 560px;
  width: 240px;
  margin: 0 5px; /* 왼쪽 오른쪽 여백으로 간격을 조절할 수 있습니다. */
  color: rgb(221, 179, 245);
  background-color: rgba(204, 0, 255, 0.1);
  /* border: 1.5px solid white; */
  border-radius: 20px;
  transition: transform 0.2s, box-shadow 0.2s;
  box-sizing: border-box; /* 너비와 높이에 padding과 border를 포함시킵니다. */
  display: inline-block; /* 인라인 블록 요소로 배치합니다. */
  vertical-align: top; /* 맨 위에 정렬합니다. */
}

.card:hover {
  transform: translateY(-15px); /* 왼쪽 위 대각선으로 -5px만큼 이동하여 튀어나오는 효과 생성 */
  box-shadow: 10px 10px 10px rgba(0, 0, 0, 0.3); /* 테두리에 그림자 추가 */
}

.card-avatar {
  border-radius: 40px;
  width: 100%;
  height: auto;
}
.card-title {
  font-weight: bold;
  margin-bottom: 0.5rem;
  font-size: 1.5rem;
  text-align: center;
}
.card-content {
  display: flex;
  justify-content: space-between;
  font-weight: bold;
}

.card a,
.card a:hover {
  color: inherit;
  text-decoration: none;
}
</style>
