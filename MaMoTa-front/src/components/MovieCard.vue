<template>
  <div class="col-lg-3 col-md-6 col-sm-6">
    <div class="card h-100">
      <div :data-bs-target="'#staticBackdrop' + movie.id" data-bs-toggle="modal">
        <img :src="getImageUrl(movie.poster_path)" class="card-img-top" alt="#" >
      </div>

      <div :id="'staticBackdrop' + movie.id" class="modal fade" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
        aria-labelledby="staticBackdropLabel" aria-hidden="true">
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
import MovieDetailInfo from '@/components/MovieDetailInfo.vue';

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
</style>
