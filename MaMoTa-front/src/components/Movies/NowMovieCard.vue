<template>
  <div class="col-lg-2 col-md-4 col-sm-4">
    <div class="card h-100 position-relative movie-card">
      <div :data-bs-target="'#staticBackdrop' + movie.id" data-bs-toggle="modal">
        <div class="custom-poster-container">
          <img :src="getImageUrl(movie.poster_path)" class="card-img-top custom-poster" alt="#">
          <div class="title-overlay"></div>
          <div class="title-text">{{ movie.title || movie.name }}</div>
        </div>
      </div>

      <div :id="'staticBackdrop' + movie.id" class="modal fade" data-bs-backdrop="static" data-bs-keyboard="false"
        tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="staticBackdropLabel">{{ movie.title || movie.name }}</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <MovieDetailInfo :movie="movie" />
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import MovieDetailInfo from '@/components/Movies/MovieDetailInfo.vue';

const props = defineProps(["movie"])

const getImageUrl = (path) => {
  if (!path) {
    return '/src/assets/Images/img_no_poster.png';
  }
  return `https://image.tmdb.org/t/p/w300${path}`;
}
</script>

<style scoped>

.movie-card {
  background-color: black;
}

.card-overview {
  color: black;
  text-decoration: none;
}

.custom-poster-container {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 150%; /* 3:2 비율로 조절, 100% * (2/3) */
  overflow: hidden;
}

.custom-poster {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover; /* 이미지가 꽉 차게 보이도록 */
}

.title-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background: linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.7)); /* 그라데이션으로 투명도 조절 가능 */
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
  text-align: center; /* 가운데 정렬 */
}

.modal-content {
  background-color: black;
  color: white;
}

.btn-close {
  background-color: white;
}

.modal-header, .modal-footer {
  border-color: rgb(233, 42, 233);
}
</style>
