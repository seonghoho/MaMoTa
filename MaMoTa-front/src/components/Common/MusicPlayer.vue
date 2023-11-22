<template>
  <div class="music-player">
    <div class="video-container">
      <iframe
        ref="videoIframe"
        width="100%"
        height="100%"
        :src="currentVideo"
        frameborder="0"
        allowfullscreen
        :isPlaying="true"
        class="video-iframe"
      ></iframe>
    <div class="controls">
      <button @click="playPrevious" class="control-button">
        <font-awesome-icon :icon="['fas', 'backward']" size="xl" style="color: white;" />
      </button>
      
      <div class="controls">
      <div class="current-audio"><strong>{{ getCurrentAudioTitle() }}</strong></div>
    </div>
      <button @click="playNext" class="control-button foward">
        <font-awesome-icon :icon="['fas', 'forward']" size="xl" style="color: white;" />
      </button>
    </div>
    
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useMusicStore } from '@/stores/music';

const store = useMusicStore();

const audios = store.audios;
const isPlaying = ref(false);
const videoIframe = ref(null);

let currentIndex = 0;

const currentVideo = ref(audios[currentIndex]);

const playNext = () => {
  currentIndex = (currentIndex + 1) % audios.length;
  currentVideo.value = audios[currentIndex];
  isPlaying.value = true;
};

const playPrevious = () => {
  currentIndex = (currentIndex - 1 + audios.length) % audios.length;
  currentVideo.value = audios[currentIndex];
  isPlaying.value = true;
};


const getCurrentAudioTitle = () => {
  return audios[currentIndex].replace(/^.*[\\\/]/, '').replace(/\.[^/.]+$/, '');
};


onMounted(() => {
  window.addEventListener('message', handleIframeMessages);

  videoIframe.value.addEventListener('ended', () => {
    playNext();
  });
});

const handleIframeMessages = (event) => {
  if (event.source !== videoIframe.value.contentWindow) {
    return;
  }

  const data = JSON.parse(event.data);
  if (data.event === 'pause') {
    isPlaying.value = false;
  } else if (data.event === 'play') {
    isPlaying.value = true;
  }
};
</script>

<style scoped>
@keyframes marquee {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(-100%);
  }
}
.music-player {
  margin-bottom: 20px;
  width: 470px;
  text-align: center;
  padding: 10px;
  color: white;
  border: 2px solid rgb(233, 42, 233);
  border-radius: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 999;
  background: url('@/assets/Images/musicbackground.gif') no-repeat;
  background-position: -10%;
  background-size: cover;
}

.foward {
  margin-left: 20px;
}
.controls {
  display: flex;
  margin-top: 30px;
  margin-left: 40px;
  margin-right: 50px;
}
.control-button {
  background-color: transparent;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  font-size: 18px;
  border-radius: 5px;
}

.video-container {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 14.25%; 
  margin: auto;
  transform: translateY(-60%);
  margin-top: 20px; /* 아래로 내리기 위한 여백 */
}
.video-iframe {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 70%;
  border: none;
  min-height: 50px;
  margin-top: 20px;
  transform: translateY(50%);
  visibility: hidden;
}

.current-audio {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  margin-right: 0px;
  font-size: 20px;
  transform: translateY(-40%);
}
</style>
