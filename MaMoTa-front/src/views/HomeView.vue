<template>
  <div>
    <NowPlayingView />
    <PopularMovieView />
    <TopRatedMovieView />
    <UpComingView />
    <RomanceMovieView />
    <SFMovieView />    
    <AnimationMovieView />
    <ActionMovieView />
    <HororMovieView />
    <CriminalMovieView />
    <WarMovieView />
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
import SFMovieView from '@/views/Genres/SFMovieView.vue';
import AnimationMovieView from '@/views/Genres/AnimationMovieView.vue';
import RomanceMovieView from '@/views/Genres/RomanceMovieView.vue';
import ActionMovieView from '@/views/Genres/ActionMovieView.vue';
import HororMovieView from '@/views/Genres/HororMovieView.vue';
import WarMovieView from '@/views/Genres/WarMovieView.vue';
import CriminalMovieView from '@/views/Genres/CriminalMovieView.vue';
import TopButton from '@/components/Common/TopButton.vue';

</script>

<style scoped>

</style>
