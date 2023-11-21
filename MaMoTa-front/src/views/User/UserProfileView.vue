<template>
  <div v-if="user">
    <div class="profile-container">
      <div>
        <ul class="nav justify-content-center">
          <li class="nav-item linkname">
            <RouterLink
              :to="`/user/profile/${user.id}/info`"
              class="nav-link"
            >
              <h3>회원정보</h3>
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              :to="`/user/profile/${user.id}/pick`"
              class="nav-link"
            >
              <h3>좋아하는 영화</h3>
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              :to="`/user/profile/${user.id}/article`"
              class="nav-link"
            >
              <h3>작성한 게시글</h3>
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              :to="`/user/profile/${user.id}/follower`"
              class="nav-link"
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

const isCurrentUser = computed(() => {
  return loggedInUserId.value === userId.value
})

const fetchUserProfile = async () => {
  try {
    let idToFetch = isCurrentUser.value ? loggedInUserId.value : userId.value;
    const response = await axios.get(`http://127.0.0.1:8000/profile/${idToFetch}/`);
    user.value = response.data;
  } catch (error) {
    alert(error);
    throw error;
  }
};

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


.nav-link h3 {
  color: white;
}
.nav-link h3:hover {
  color: rgb(213, 169, 255);
  font-weight: bolder;
  margin-top: -5px;
  margin-left: -3px;
  text-shadow: 10px 10px 10px #000;
}


</style>
