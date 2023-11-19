<template>
  <div class="app">
    <NavBar />
    <TopButton />

    <RouterView />

    <div
      class="fixed mb-2"
      data-bs-toggle="modal"
      data-bs-target="#openAiModal"
      aria-controls="openAiModal"
      style="position: fixed; bottom: 0; left: 15px; cursor: pointer;"
    >
      <img class="rounded-circle icon" src="@/assets/Images/Ai_Icon.gif" alt="Ai_Icon">
    </div>

    <div id="openAiModal" class="modal fade" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
      aria-labelledby="openAiModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="openAiModalLabel">🎞 무피티</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <OpenAi />
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import NavBar from '@/components/Common/NavBar.vue';
import OpenAi from '@/components/Common/OpenAi.vue';
import TopButton from '@/components/Common/TopButton.vue';
import { RouterView } from 'vue-router';


</script>

<style scoped>
.icon {
  width: 50px;
  height: 50px;
  object-fit: cover;
}
h2 {
  text-align: center;
  margin-top: 15px;
}
.app {
  background-color: black;
}


</style>
