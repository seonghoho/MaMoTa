<template>
  <div>
    <div class="card h-100 position-relative movie-card">
      <div class="custom-poster-container">
        <RouterLink :to="{ name: 'movie', params: { id: movie.id || movie.pk } }">
          <img :src="getImageUrl(movie.poster_path)" class="card-img-top" alt="..." />
          <div class="card-body text-center">
            <div class="title-overlay"></div>
            <div class="title-text">{{ movie.title || movie.name }}</div>
          </div>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  movie: Object
})

const getImageUrl = (path) => {
  // 이미지가 없는경우 예외처리
  if (!path) {
    return '/src/assets/Images/img_no_poster.png';
  }
  return `https://image.tmdb.org/t/p/w500${path}`
}

const getFormattedTitle = computed(() => {
  const title = props.movie.title || props.movie.name
  return title.length > 15 ? title.slice(0, 15) + '...' : title
})
</script>

<style scoped>
.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card a,
.card a:hover {
  color: inherit;
  text-decoration: none;
}

.movie-card {
  background-color: black;
  border-radius: 20px;
  transition: transform 0.2s, box-shadow 0.2s;
  
}

.movie-card:hover {
  transform: translateY(-15px); /* 왼쪽 위 대각선으로 -5px만큼 이동하여 튀어나오는 효과 생성 */
  box-shadow: 10px 10px 10px rgba(0, 0, 0, 0.3); /* 테두리에 그림자 추가 */
}



.card-overview {
  color: black;
  text-decoration: none;
}

.custom-poster-container {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 150%;
  /* 3:2 비율로 조절, 100% * (2/3) */
  overflow: hidden;
}

.custom-poster {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
  /* 이미지가 꽉 차게 보이도록 */
}

.title-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.7));
  /* 그라데이션으로 투명도 조절 가능 */
}

.title-text {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 16px;
  color: white;
  font-size: 18px;
  font-weight: bold;
  text-align: center;
  /* 가운데 정렬 */
}</style>
