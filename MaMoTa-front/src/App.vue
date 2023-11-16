<template>
  <div>
    <NavBar />

    <button
      class="btn btn-primary fixed-bottom start-0 mb-2"
      type="button"
      data-bs-toggle="modal"
      data-bs-target="#openAiModal"
      aria-controls="openAiModal"
    >
      OpenAI
    </button>

    <div id="openAiModal" class="modal fade" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
      aria-labelledby="openAiModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="openAiModalLabel">OpenAI</h1>
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
  <RouterView />
</template>

<script setup>
import NavBar from '@/components/Common/NavBar.vue';
import OpenAi from '@/components/Common/OpenAi.vue';
import { RouterView } from 'vue-router';
</script>

<style scoped></style>
