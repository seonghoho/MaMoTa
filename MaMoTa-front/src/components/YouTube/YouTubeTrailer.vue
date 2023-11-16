<template>
  <div>
    <div id="player">
      <iframe
        :class="['youtube-iframe', screenClass]"
        :src="getVideoUrl()"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, defineComponent, reactive, watch, onMounted, defineProps } from "vue";
import axios from "axios";

export default defineComponent({
  props: {
    movieTitle: String,
  },
  setup(props) {
    const state = reactive({
      videoId: "",
    });

    const fetchTrailer = () => {
      const youtubeKey = import.meta.env.VITE_YOUTUBE_API_KEY;
      const baseURL = "https://www.googleapis.com/youtube/v3/search";
      axios
        .get(baseURL, {
          params: {
            key: youtubeKey,
            part: "snippet",
            type: "video",
            q: props.movieTitle + "공식 예고편",
            maxResults: 1,
          },
        })
        .then((response) => {
          const videoId = response.data.items[0].id.videoId;
          state.videoId = videoId;
        })
        .catch((error) => {
          console.error("서버에러:", error);
        });
    };

    onMounted(() => {
      fetchTrailer();
    });

    watch(() => state.videoId, () => {
      fetchTrailer();
    });

    const getVideoUrl = () => {
      return `https://www.youtube.com/embed/${state.videoId}?autoplay=1&mute=1`;
    };

    const screenClass = ref("sm");

    const updateScreenClass = () => {
      const screenWidth = window.innerWidth;
      if (screenWidth < 576) {
        screenClass.value = "xs";
      } else if (screenWidth < 768) {
        screenClass.value = "sm";
      } else if (screenWidth < 992) {
        screenClass.value = "md";
      } else if (screenWidth < 1200) {
        screenClass.value = "lg";
      } else {
        screenClass.value = "xl";
      }
    };

    onMounted(() => {
      updateScreenClass();
    });

    window.addEventListener("resize", updateScreenClass);

    return {
      state,
      getVideoUrl,
      screenClass,
    };
  },
});
</script>

<style scoped>
.youtube-iframe {
  width: 100%;
}

@media (min-width: 576px) {
  .sm {
    height: 250px;
  }
}

@media (min-width: 768px) {
  .md {
    height: 400px;
  }
}

@media (min-width: 992px) {
  .lg {
    height: 500px;
  }
}

@media (min-width: 1200px) {
  .xl {
    height: 600px;
  }
}
</style>
