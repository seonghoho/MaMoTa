<template>
  <div class="profile-container bg-light text-dark rounded mt-5 p-4">
    <!-- 프로필 사진
    <div class="profile-pic-container mb-4 text-center">
      <img
        :src="user.profile_pic ? userProfilePic : AvatarSrc"
        alt="No Image"
        class="profile-pic rounded-circle shadow"
      />
    </div> -->
    <!-- 사용자 정보 -->
    <div class="text-center mb-4">
      <h3 class="mb-0">{{ user.nickname }}</h3>
    </div>
    <div class="user-details border-top pt-3">
      <div class="like-count-info mb-2">
        리뷰 수: <strong>{{ user.articles_count }}</strong>
      </div>
      <div class="like-count-info mb-2">
        좋아요 수: <strong>{{ user.like_count }}</strong>
      </div>
      <div class="like-count-info mb-2">
        가입일: <strong>{{ formattedDateJoined }}</strong>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, computed } from 'vue'
import AvatarSrc from '@/assets/avatar.png'

const props = defineProps(['user'])

const username = computed(() => props.user.username.split('@')[0])
const userProfilePic = computed(() => `http://localhost:8000${props.user.profile_pic}`)

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
  max-width: 500px;
  min-width: 300px;
  margin: 0 auto;
}

.profile-pic-container {
  position: relative;
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
