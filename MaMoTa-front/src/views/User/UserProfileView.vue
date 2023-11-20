<template>
  <div v-if="user">
    <div class="profile-container">
      <div>
        <ul class="nav justify-content-center">
          <li v-if="isCurrentUser" class="nav-item">
            <RouterLink
              :to="`/user/profile/${user.id}/info`"
              class="nav-link"
              :class="{
                'text-info': $route.path.includes(`${user.id}/info`),
                'text-secondary': !$route.path.includes(`${user.id}/info`)
              }"
            >
              <h3>회원정보</h3>
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              :to="`/user/profile/${user.id}/pick`"
              class="nav-link"
              :class="{
                'text-info': $route.path.includes(`${user.id}/pick`),
                'text-secondary': !$route.path.includes(`${user.id}/pick`)
              }"
            >
              <h3>좋아하는 영화</h3>
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              :to="`/user/profile/${user.id}/article`"
              class="nav-link"
              :class="{
                'text-info': $route.path.includes(`${user.id}/article`),
                'text-secondary': !$route.path.includes(`${user.id}/article`)
              }"
            >
              <h3>작성리뷰</h3>
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              :to="`/user/profile/${user.id}/follower`"
              class="nav-link"
              :class="{
                'text-info': $route.path.includes(`${user.id}/follower`),
                'text-secondary': !$route.path.includes(`${user.id}/follower`)
              }"
            >
              <h3>팔로우</h3>
            </RouterLink>
          </li>
        </ul>
      </div>
      <RouterView :user="user" :isCurrentUser="isCurrentUser"></RouterView>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, onBeforeRouteUpdate } from 'vue-router'
import { userProfileApi } from '@/apis/userApi'
import axios from 'axios';

const user = ref(null)
const route = useRoute()
const userId = ref(route.params.userId)
const loggedInUserId = ref(localStorage.getItem('userPk'))
console.log(loggedInUserId.value)
console.log(userId.value)

const isCurrentUser = computed(() => {
  return loggedInUserId.value === userId.value
})

onBeforeRouteUpdate((to, from, next) => {
  if (to.params.userId !== from.params.userId) {
    userId.value = to.params.userId
    fetchUserProfile()
      .then(() => {
        next()
      })
      .catch((err) => {
        alert(err)
        next()
      })
  } else {
    next()
  }
})

const fetchUserProfile = async () => {
  try {
    let idToFetch = isCurrentUser.value ? loggedInUserId.value : userId.value;
    console.log(idToFetch);
    const response = await axios.get(`http://127.0.0.1:8000/profile/${idToFetch}/`);
    console.log(response.data);
    user.value = response.data; // user에 response.data를 할당
    console.log(user.value)
  } catch (error) {
    alert(error);
    throw error; // throw를 통해 호출자에게 에러를 전파합니다.
  }
};


onMounted(fetchUserProfile)
</script>

<style scoped>
.profile-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  margin: 0 auto;
}
</style>
