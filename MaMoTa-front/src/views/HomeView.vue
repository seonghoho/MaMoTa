<template>
  <div>
    <NowPlayingView />
    <PopularMovieView />
    <TopRatedMovieView />
    <UpComingView />
    <TopButton />

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { RouterLink } from 'vue-router';
import UpComingView from '@/views/Movies/UpComingView.vue';
import TopRatedMovieView from '@/views/Movies/TopRatedMovieView.vue';
import PopularMovieView from '@/views/Movies/PopularMovieView.vue';
import NowPlayingView from '@/views/Movies/NowPlayingView.vue';
import TopButton from '@/components/Common/TopButton.vue';


</script>

<style scoped>

</style>
