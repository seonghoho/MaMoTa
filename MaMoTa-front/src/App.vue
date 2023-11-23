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
        <div class="modal-content ai-modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="openAiModalLabel">🎞 무피티</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <OpenAi />
          </div>
        </div>
      </div>
    </div>

    <div
      class="fixed mb-2"
      data-bs-toggle="modal"
      data-bs-target="#MusicModal"
      aria-controls="MusicModal"
      style="position: fixed; bottom: 0; right: 30px; cursor: pointer;"
    >
      <img class="rounded-circle icon" src="@/assets/Images/PlayButton.gif" alt="Ai_Icon">
    </div>

<div class="modal fade" id="MusicModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">OST Player</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <MusicPlayer />
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
import MusicPlayer from '@/components/Common/MusicPlayer.vue';

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

.modal-content {
  background-color: black;
  color: white;
  border-color: rgb(233, 42, 233)
}

.ai-modal-content {
  background: url('@/assets/Images/ai-modal.gif') no-repeat;
  background-size: cover;
}

.modal-header {
  border-color: rgb(233, 42, 233);
}

.modal-footer {
  border-color: rgb(233, 42, 233);
}

.btn-close {
  background-color: rgb(233, 42, 233);
}

@font-face {
    font-family: 'Giants-Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2307-1@1.1/Giants-Bold.woff2') format('woff2');
    font-weight: 700;
    font-style: normal;
}

* {
  font-family:'Giants-Bold';
}

</style>
