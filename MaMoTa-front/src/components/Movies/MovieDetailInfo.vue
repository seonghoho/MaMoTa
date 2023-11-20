<template>
  <div>

    <div class="poster-container">
      <img :src="getImageUrl(movie.poster_path)" class="card-img-top poster" alt="#">
      <div class="movie-info">
        <h1>{{ movie.title }}</h1>
        <div>
          <p>개봉일 : {{ movie.release_date }}</p>
          <p>TMDB 평점 : {{ movie.vote_average }}</p>
        </div>

        <h3>장르</h3>
        <ul>
          <li v-for="genreId in movie.genre_ids" :key="genreId">
            {{ getGenreNameById(genreId) }}
          </li>
        </ul>

        <div>
          <h3>줄거리</h3>
          <p>{{ movie.overview }}</p>
        </div>
      </div>
    </div>    
    <div class="trailer">
      <h3>예고편</h3>
      <!-- <YoutubeTrailer :movieTitle="movie.title" /> -->
    </div>
  </div>
</template>

<script setup>
import YoutubeTrailer from '@/components/YouTube/YoutubeTrailer.vue';
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

const props = defineProps(["movie"]);

const getImageUrl = (path) => {
  if (!path) {
    return '';
  }
  return `https://image.tmdb.org/t/p/w300${path}`;
}

const getGenreNameById = (genreId) => {
  const foundGenre = store.genre.genres.find(genre => genre.id === genreId);
  return foundGenre ? foundGenre.name : 'Unknown Genre';
}
</script>

<style>
.poster {
  max-width: 300px;
  max-height: 450px;
}

.poster-container {
  display: flex;
  align-items: center;
}

.movie-info {
  margin-left: 20px;
}

@media (max-width: 1000px) {
  .poster-container {
    flex-direction: column;
  }

  .movie-info {
    margin-left: 0;
    margin-top: 20px;
  }
}

.trailer {
  margin-top: 15px;
}

</style>