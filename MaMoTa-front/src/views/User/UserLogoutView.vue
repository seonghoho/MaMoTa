<template>
  <div class="mylogout"></div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/userStore'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'

const userStore = useUserStore()
const router = useRouter()

const alertMessage = () => {
  Swal.fire({
    title: '로그아웃 하시겠습니까?',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#810CA8',
    cancelButtonColor: '#FA2FB5',
    confirmButtonText: '로그아웃',
    cancelButtonText: '취소',
    // 보라색
    background: '#D1C4E9',
    backdrop: "rgba(0,0,123,0.4) url('/src/assets/Images/nyan_cat.gif')  center top",

    
  }).then((result) => {
    // 로그아웃 Yes , No 두 경우 모두다 home으로 이동
    if (result.isConfirmed) {
      logout()
    }
    router.push({ name: 'home' })
  })
}

const logout = () => {
  userStore.logout()
}

onMounted(() => {
  if (userStore.isLogin) {
    alertMessage()
  } else {
    Swal.fire('잘못된 접근입니다.', '', 'error')
    router.back()
  }
})
</script>

<style scoped>
.mylogout {
  background-color: black;
  min-height: 100vh;
  color: white;
}
</style>
