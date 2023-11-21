<template>
  <div class="container">
    <div class="d-flex">
      <input
        :value="title"
        @input="inInput"
        v-on:keyup.enter="searchMovie"
        class="form-control me-2 search-input"
        type="search"
        placeholder="검색어를 입력하세요!"
        aria-label="Search"
      />
      <button @click="searchMovie" class="btn btn-outline-success search-button">Search</button>
    </div>
    <h1 class="title">{{ movieTitle }} 검색결과</h1>
    <div class="row row-cols-1 row-cols-md-4 g-4">
      <NowMovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import NowMovieCard from '@/components/Movies/NowMovieCard.vue';

const route = useRoute()
const movieTitle = ref(route.query.movieTitle || '')
const title = ref('')
const router = useRouter()

const movies = ref([])
const key = import.meta.env.VITE_TMDB_API_KEY


const fetchMovie = () => {
  const url = `https://api.themoviedb.org/3/search/movie?query=${movieTitle.value}&include_adult=false&language=ko-Kr&page=1`;
  const headers = {
    Accept: 'application/json',
    Authorization: `Bearer ${key}`,
  };

  axios.get(url, { headers })
    .then((response) => {
      movies.value = response.data.results.slice(0, 10);
    })
    .catch((err) => {
      alert('Axios Error: ' + err.message);
    });
};

watch(() => route.query.movieTitle, (newValue, oldValue) => {
  movieTitle.value = newValue || ''
  location.reload()
})

const inInput = (event) => {
  title.value = event.currentTarget.value
}

const searchMovie = () => {
  router.push({ path: '/search', query: { movieTitle: title.value } })
}

onMounted(fetchMovie)

</script>

<style scoped>
.title {
  color: white;
}

.search-input {
  margin-top: 15px;
  background-color: black;
  color: white;
  border: 1px solid rgb(233, 42, 233);
}

.search-input::placeholder {
  color: white;
}
.search-button {
  margin-top: 15px;
  background-color: black;
  color: white;
  border: 1px solid rgb(233, 42, 233);
}
</style>