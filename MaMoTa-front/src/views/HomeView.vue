<template>
  <div>
    <select v-model="selectedOption" @change="navigateToView">
      <option value="popular">인기순</option>
      <option value="top_rated">평점순</option>
    </select>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const selectedOption = ref()
const router = useRouter()

const navigateToView = () => {
  const viewName = selectedOption.value === 'popular' ? 'PopularMovieView' : 'TopRatedMovieView'
  router.push({ name: viewName })
}
</script>

<style scoped>

</style>
