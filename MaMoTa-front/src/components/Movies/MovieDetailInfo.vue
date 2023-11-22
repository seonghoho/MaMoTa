<template>
  <div>
    <div class="poster-container" :style="`backgroundImage:url('${getImageUrl(movie.backdrop_path)}')`">
      <img :src="getImageUrl(movie.poster_path)" class="card-img-top poster" alt="#">
      <div class="movie-info">
        <h1>{{ movie.title }}</h1>
        <div>
          <p>개봉일 : {{ movie.release_date }}</p>
          <p>🔥 {{ movie.vote_average }} / 10</p>
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
    <div class="separator"></div>
    <RouterLink :to="{ name: 'articleCreate', query: { movie_title: `${ movie.title }`} }">
      게시글 작성
    </RouterLink>
    <div class="separator"></div>
    <div class="trailer">
      <h3>예고편</h3>
      <div class="iframe-container">
      <iframe 
      width="1080" 
      height="720" 
      :src="`https://www.youtube.com/embed/${videoKey}`" 
      title="YouTube video player" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
      allowfullscreen></iframe>
      </div>
    </div>
    <div class="separator"></div>
    <div class="director">
      <h3>감독</h3>
      <img :src="getImageUrl(directorCredit.profile_path)" class="profile" alt="#">
      <p>{{ directorCredit.name }}</p>

    </div>
    <div>
      <h3 class="actor-data">배우</h3>
      <div class="actors">
        <div v-for="actor in actorCredit" :key="actor.id" class="actor">
          <img :src="getImageUrl(actor.profile_path)" class="profile" alt="#">
          <p class="actor-data">{{ actor.name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, ref, onMounted } from 'vue';
import axios from 'axios';
import { RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore();

const props = defineProps(["movie"]);
const key = import.meta.env.VITE_TMDB_API_KEY;
const credits = ref([]);
const directorCredit = ref({});
const actorCredit = ref({});
const videos = ref([]);
const videoKey = ref('');

const getImageUrl = (path) => {
  if (!path) {
    return '/src/assets/Images/img_no_poster.png';
  }
  return `https://image.tmdb.org/t/p/w300${path}`;
}

const getGenreNameById = (genreId) => {
  const foundGenre = store.genre.genres.find(genre => genre.id === genreId);
  return foundGenre ? foundGenre.name : 'Unknown Genre';
}

const fetchCredit = () => {
  const url = `https://api.themoviedb.org/3/movie/${props.movie.id}/credits?language=ko-KR`;
  const headers = {
    Accept: 'application/json',
    Authorization: `Bearer ${key}`,
  };

  axios.get(url, { headers })
    .then((response) => {
      credits.value = response.data || [];
      directorCredit.value = response.data.crew.find(credit => credit.known_for_department === "Directing") || {};
      actorCredit.value = response.data.cast.slice(0, 6);
    })
    .catch((err) => {
      console.log('Axios Error: ' + err.message);
    });
};

const fetchVideo = () => {
  const url = `https://api.themoviedb.org/3/movie/${props.movie.id}/videos?language=ko-KR`;
  const headers = {
    Accept: 'application/json',
    Authorization: `Bearer ${key}`,
  };

  axios.get(url, { headers })
    .then((response) => {
      videos.value = response.data.results[0];
      videoKey.value = videos.value?.key || ''; 
    })
    .catch((err) => {
      console.log('Axios Error: ' + err.message);
    });
};


// console.log(credits)
// console.log(actorCredit)
// console.log(videos)


onMounted(fetchCredit);
onMounted(fetchVideo);
</script>

<style>
.poster {
  max-width: 300px;
  max-height: 450px;
}

.detail,
.movie-info,
.h3,
.p {
  color: white !important;
}

.profile {
  max-width: 150px;
  max-height: 275px;
}

.actors {
  display: flex;
  gap: 20px;
  overflow-x: auto;
}

.actor {
  text-align: center;
  flex: 0 0 auto;
  color: white !important;
}

.director {
  color: white !important;
}

.actor-data {
  color: white !important;
}

.separator {
  border: none;
  border-top: 2px solid rgb(233, 42, 233);
  margin: 20px 0;
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
  position: relative;
}

.iframe-container {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%;
}

iframe {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0; 
}

</style>