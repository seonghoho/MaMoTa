<template>
    <div class="carousel-container">
      <h3 class="title">🤖 I'm your father</h3>
      <div class="arrow left" @click="prev">&lt;</div>
  
      <div class="carousel">
        <MovieCard
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
          class="card"
        />
      </div>
      <div class="arrow left" @click="prev">&lt;</div>
      <div class="arrow right" @click="next">&gt;</div>
    </div>
  </template>
  
  <script setup>
  import MovieCard from '@/components/Movies/MovieCard.vue'
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const key = import.meta.env.VITE_TMDB_API_KEY;
  const movies = ref([]);
  const cardWidth = 200; // Adjust the width as needed
  const numVisibleCards = 5;
  const totalCards = 50; // Set the total number of cards
  
  const fetchMovie = () => {
    const url = 'https://api.themoviedb.org/3/discover/movie?with_genres=878&language=ko-KR&page=1';
    const headers = {
      Accept: 'application/json',
      Authorization: `Bearer ${key}`,
    };
  
    axios.get(url, { headers })
      .then((response) => {
        movies.value = response.data.results.slice(0, totalCards);
      })
      .catch((err) => {
        alert('Axios Error: ' + err.message);
      });
  };
  
  onMounted(() => {
    fetchMovie();
  });

  const prev = () => {
    movies.value.push(movies.value.shift());
  };
  
  const next = () => {
    movies.value.unshift(movies.value.pop());
  };
  
  </script>
  
  <style scoped>
  .title {
    margin-left: 20px;
    color: white;
  }
  .carousel-container {
    margin-top: 25px;
    position: relative;
    width: 100%;
  }
  
  .carousel {
    display: flex;
    gap: 10px; /* Adjust the gap between cards */
    transition: transform 0.5s ease-in-out;
    padding: 10px; /* Add padding for better visibility */
  }
    
  .arrow {
    position: absolute;
    top: 50%;
    font-size: 24px;
    color: white;
    cursor: pointer;
    user-select: none;
    padding: 10px;
    border: none;
    outline: none;
    transition: background 0.3s ease-in-out;
  }
  
  .left {
    left: 10px;
    background: linear-gradient(90deg, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0) 100%);
    padding: 10px;
    border-radius: 5px;
  }
  
  .right {
    right: 10px;
    background: linear-gradient(90deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.5) 100%);
    padding: 10px;
    border-radius: 5px;
  }
  </style>
  