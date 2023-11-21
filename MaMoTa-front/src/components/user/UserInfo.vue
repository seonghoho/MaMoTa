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
        <strong>좋아요 수: {{ user.like_count }}</strong>
      </div>
      <div class="like-count-info mb-2">
        <strong>팔로워 수: {{ user.follower_count }}</strong>
      </div>

    </div>
  </div>
</template>

<script setup>
import { defineProps, computed } from 'vue'
// import AvatarSrc from '@/assets/avatar.png'

const props = defineProps(['user'])

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
  height: 280px;
  margin: 0 auto;
  color: rgb(221, 179, 245);
  transition: transform 0.2s, box-shadow 0.2s;
}

.profile-container:hover {
  transform: translateY(-5px); /* 왼쪽 위 대각선으로 -5px만큼 이동하여 튀어나오는 효과 생성 */
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
</style>
