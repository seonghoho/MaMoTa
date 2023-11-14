<template>
  <div class="col-lg-3 col-md-6 col-sm-6">
    <div class="card h-100 ">
      <img :src="getImageUrl(movie.poster_path)" class="card-img-top" alt="#">
      <div class="card-body">
        <h5 class="card-title">{{ movie.tile || movie.name }}</h5>
        <div class="card-title card-overview">{{ movie.overview }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps(["movie"])

const getImageUrl = (path) => {
  return path ? `https://image.tmdb.org/t/p/w500${path}` : ""
}

</script>

<style scoped>
.card-overview {
  color: black;
  text-decoration: none;
}

.router-link {
  text-align: center;
}
</style>