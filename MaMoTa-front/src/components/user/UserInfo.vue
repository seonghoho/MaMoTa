<template>
  <div class="profile-container rounded mt-5 p-4" style="background-color: rgba(0, 0, 0, 0.4); border:1.5px solid white">

    <div class="text-center mb-4" v-if="!user.is_superuser">
      <h3 class="nickname mb-0">{{ user.nickname }}</h3>
    </div>
    <div class="text-center mb-4" v-else>
      <h3 class="nickname mb-0">관리자님 환영합니다.</h3>
    </div>
    <div class="user-details border-top pt-4">
      <div class="like-count-info mb-2">
        <strong>리뷰 수: {{ user.articles_count }}</strong>
      </div>
      <div class="like-count-info mb-2">
        <strong>좋아요 누른 영화 수: {{ user.like_movies_count }}</strong>
      </div>
      <div class="like-count-info mb-2">
        <strong>팔로워 수: {{ user.follower_count }}</strong>
      </div>
      <div class="like-count-info mb-2">
        <strong>팔로잉 수: {{ user.following_count }}</strong>
      </div>
      <div>
        <button
          v-show="!isCurrentUser"
          :class="isFollowing ? 'btn btn-outline-info mb-5 unfollow_button' : 'btn btn-info mb-5 follow_button'"
          @click="followUnfollow"
          style="width: 140px"
        >
          <i
            :class="isFollowing ? 'bi bi-person-dash' : 'bi bi-person-plus'"
            style="font-size: 1.25rem; vertical-align: middle; margin-right: 1rem"
          ></i>
          {{ isFollowing ? '언팔로우' : '팔로우' }}
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { defineProps, computed } from 'vue'
// import AvatarSrc from '@/assets/avatar.png'


import { ref, watchEffect } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AvatarSrc from '@/assets/avatar.png'
import { followApi } from '@/apis/userApi'
import { useUserStore } from '@/stores/userStore'
import { RouterLink } from 'vue-router'

const props = defineProps(['user', 'isCurrentUser'])

const route = useRoute()
const router = useRouter()

const userStore = useUserStore()

const userId = route.params.userId
// const userProfilePic = (path) => `http://localhost:8000${path}`
const loggedInUserId = parseInt(localStorage.getItem('userPk'))

// following logic
const isFollowing = ref(false)

const checkFollowing = () => {
  isFollowing.value = props.user.followers.some((follower) => follower.id === loggedInUserId)
}

watchEffect(() => {
  checkFollowing()
})

const followUnfollow = () => {
  const token = localStorage.getItem('token')

  // 로그인 안 한 경우 redirect
  if (!userStore.isLogin) {
    const userConfirmation = window.confirm(
      '로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?'
    )
    if (userConfirmation) {
      router.push({ name: 'userLogin' })
    }
    return
  }

  followApi(token, userId)
    .then((response) => {
      if (response.status === 200) {
        props.user.followers = response.data.followers
        props.user.followings = response.data.followings
        isFollowing.value = response.data.followers.some(
          (follower) => follower.id === loggedInUserId
        )
        props.user.follower_count = response.data.follower_count
      }
    })
    .catch((error) => {
      console.error('Error following/unfollowing user:', error)
    })
}



// const username = computed(() => props.user.username.split('@')[0])
// const userProfilePic = computed(() => `http://localhost:8000${props.user.profile_pic}`)

const formattedDateJoined = computed(() => {
  const date = props.user.date_joined ? new Date(props.user.date_joined) : null;
  return date ? new Intl.DateTimeFormat('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(date) : '';
})
</script>

<style scoped>
.profile-container {
  max-width: 400px;
  min-width: 300px;
  height: 330px;
  margin: 0 auto;
  color: rgb(221, 179, 245);
  transition: transform 0.2s, box-shadow 0.2s;
}

.profile-container:hover {
  transform: translateY(-15px); /* 왼쪽 위 대각선으로 -5px만큼 이동하여 튀어나오는 효과 생성 */
  box-shadow: 10px 10px 10px rgba(0, 0, 0, 0.3); /* 테두리에 그림자 추가 */
}


.nickname {
  font-size: 30px;
}

.like-count-info {
  font-size: 30px;
}

.profile-pic {
  width: 150px;
  height: 150px;
  object-fit: cover;
}

.user-details .like-count-info {
  font-size: 1.2em;
}

/* 팔로우버튼 색상 설정 */
.follow_button {
  background-color: rgb(191, 122, 255); 
  color: black; 
  font-weight: 600;
  border: none;
  
}
.follow_button:hover {
  background-color: #9902df;
}


/* 언팔로우버튼 색상 설정 */
.unfollow_button {
  background-color: blueviolet; 
  color: white; 
  font-weight: 600;
  border: none;
}

.unfollow_button:hover {
  background-color: #9902df;
}



</style>
