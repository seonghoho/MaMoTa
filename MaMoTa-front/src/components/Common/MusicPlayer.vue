<template>
  <div class="music-player">
    <div class="controls">
      <button @click="playPrevious" class="control-button">
        <font-awesome-icon :icon="['fas', 'backward']" style="color: #e92ae9;" />
      </button>
    </div>

    <div class="video-container">
      <iframe
        ref="videoIframe"
        width="100%"
        height="100%"
        :src="currentVideo"
        frameborder="0"
        allowfullscreen
        class="video-iframe"
      ></iframe>
    </div>

    <div class="controls">
      <button @click="playNext" class="control-button">
        <font-awesome-icon :icon="['fas', 'forward']" style="color: #e92ae9;" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import { useMusicStore } from '@/stores/music';

const store = useMusicStore();

const videos = store.videos;
const isPlaying = ref(false);
const videoIframe = ref(null);

let currentIndex = 0;

const currentVideo = ref(videos[currentIndex]);

const playNext = () => {
  currentIndex = (currentIndex + 1) % videos.length;
  console.log(currentIndex)
  currentVideo.value = videos[currentIndex];
  isPlaying.value = true;
};

const playPrevious = () => {
  currentIndex = (currentIndex - 1 + videos.length) % videos.length;
  console.log(currentIndex)
  currentVideo.value = videos[currentIndex];
  isPlaying.value = true;
};


onMounted(() => {
  // Add event listener for messages from the iframe
  window.addEventListener('message', handleIframeMessages);

  // Add event listener for iframe 'ended' event
  videoIframe.value.addEventListener('ended', () => {
    playNext();
  });
});

const handleIframeMessages = (event) => {
  // Check if the message is from the iframe
  if (event.source !== videoIframe.value.contentWindow) {
    return;
  }

  // Handle messages from the iframe
  const data = JSON.parse(event.data);
  if (data.event === 'pause') {
    isPlaying.value = false;
  } else if (data.event === 'play') {
    isPlaying.value = true;
  }
};
</script>

<style scoped>
.music-player {
  position: fixed;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  max-width: 100%; /* Initial max-width set to 100% */
  text-align: center;
  padding: 10px;
  border: 2px solid rgb(233, 42, 233);
  border-radius: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 999;
}

@media (min-width: 30em) {
  .music-player {
    max-width: 30vw;
  }
}

.controls {
  display: flex;
  justify-content: space-between;
}

.control-button {
  background-color: transparent;
  color: #e92ae9;
  border: none;
  padding: 10px;
  cursor: pointer;
  font-size: 18px;
  border-radius: 5px;
}

.video-container {
  position: relative;
  width: 40%;
  height: 0;
  padding-bottom: 14.25%; /* 16:9 비율을 유지하기 위한 값 */
  margin: auto;
  transform: translateY(-60%);
}

.video-iframe {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  border: none;
  min-height: 50px; /* 최소 높이 설정 (조절 가능) */
  transform: translateY(50%);
}
</style>
