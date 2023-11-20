<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark" data-bs-theme="dark">
      <RouterLink :to="{ name: 'home' }" class="router-link" active-class="active-tab">
        <img :src="logo" alt="Logo" height="50" width="50">
      </RouterLink>
      <RouterLink :to="{ name: 'search' }" class="search">
        <img :src="search" alt="Logo" height="50" width="50">
      </RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav align-items-end">
          <li class="nav-item">
            <RouterLink :to="{ name: 'home' }" class="router-link" active-class="active-tab">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'community' }" class="router-link" active-class="active-tab">Community</RouterLink>
          </li>

          <!-- 로그인 됐으면 -->
          
          <li class="nav-item">
            <RouterLink v-if="userStore.token" :to="`/user/profile/${userStore.userData.pk}`" 
            class="router-link" active-class="active-tab">
              Profile
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink v-if="userStore.token" to="/logout"
            class="router-link" active-class="active-tab">
              Logout
            </RouterLink>
          </li>
        
          <!-- 로그인 안 된 상태이면 -->

          <li class="nav-item">
            <RouterLink v-if="!userStore.token" to="/user/login"
            class="router-link" active-class="active-tab">
              Login
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink v-if="!userStore.token" to="/user/signup"
            class="router-link" active-class="active-tab">
              Signup
            </RouterLink>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { ref } from 'vue'
import logoSrc from '@/assets/Images/logo.png'
import searchSrc from '@/assets/Images/Search.png'

// 로그인 관련 부분
import { useUserStore } from '@/stores/userStore';
const userStore = useUserStore()

const logo = ref(logoSrc)
const search = ref(searchSrc)

</script>

<style scoped>
.navbar {
  border: 2px solid rgb(233, 42, 233);
}

.router-link {
  text-decoration: none;
  color: white;
  margin-right: 15px;
}

.active-tab {
  color: rgb(233, 42, 233) !important;
  font-weight: bold !important;
}

.search {
  margin: auto
}

</style>
