<template>
  <div class="button-top" v-show="isShow" @click="scrollToTop">
    <img src="@/assets/UpButton.png" alt="">
    <span class="blind">상단으로</span>
  </div>
</template>

<script>

export default {
  data() {
    return {
      isShow: false,
    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.isShow = window.scrollY > 100;
    },
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
  },
};
</script>

<style scoped>
img {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 50px;
  height: 55px;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: opacity 0.3s;
}
.button-top i {
  font-size: 1.5em;
}

.button-top:hover {
  opacity: 0.8;
}

.blind {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
</style>
