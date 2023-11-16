<template>
  <div>
    <div>
      <YoutubeTrailer :movieTitle="movie.title" />
    </div>
    <h1>{{ movie.title }}</h1>
    <div>
      <p>개봉일 : {{ movie.release_date }}</p>
      <p>러닝타임 : {{ movie.runtime }} 분</p>
      <p>TMDB 평점 : {{ movie.vote_average }}</p>
    </div>

    <h3>장르</h3>
    <div>
      <ul>
        <li v-for="genre in movie.genres" :key="genre.name">
          {{ genre.name }}
        </li>
      </ul>
    </div>

    <div>
      <h3>줄거리</h3>
      <p>{{ movie.overview }}</p>
    </div>

  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import YoutubeTrailer from '@/components/YouTube/YoutubeTrailer.vue';

const props = defineProps(["movie"])

const getImageUrl = (path) => {
  if (!path) {
    return '';
  }
  return `https://image.tmdb.org/t/p/w500${path}`;
}

onMounted(() => {
  getImageUrl()
})
</script>

<script scoped>

</script>