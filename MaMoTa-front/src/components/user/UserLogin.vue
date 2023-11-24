<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-12 ">
        <div class="text-center mb-4" >
          <h2>로그인</h2>
        </div>
        <div class="mb-3">
          <label for="username" class="form-label">이메일</label>
          <input
            v-model="username"
            type="username"
            class="form-control"
            id="username"
            placeholder="MaMoTa@ssafy.com"
          />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">비밀번호</label>
          <div class="input-group">
          <input
            v-model="password"
            @keyup.enter="logIn"
            type="password"
            class="form-control"
            id="password"
            placeholder="비밀번호"
            />
            <button class="btn btn-outline-secondary" type="button" @click="togglePasswordVisibility">
              <i class="bi bi-eye"></i>
            </button>
          </div>
        </div>
        <div class="d-grid gap-2">
          <button @click="logIn" class="custom-btn btn btn-info mt-4">로그인</button>
        </div>
      </div>
    </div>
  </div>
  <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/userStore'
import Swal from 'sweetalert2'

// 로그인
const username = ref(null)
const password = ref(null)
const userStore = useUserStore()

const alertMessage = (msg) => {
  Swal.fire({
    title: `${msg} 입력해주세요`,
    icon: 'error',
    confirmButtonColor: '#682cd48c',
    confirmButtonText: '확인',
    background: '#D1C4E9',
    backdrop: "rgba(0,0,123,0.4) url('/src/assets/Images/nyan_cat.gif')  center top",
  })
}

const logIn = () => {
  if (!username.value) {
    alertMessage('아이디를')
    return
  }
  if (!password.value) {
    alertMessage('비밀번호를')
    return
  }

  const payload = {
    username: username.value,
    password: password.value
  }
  // 배경색 변경 코드 추가
  document.getElementById('app').style.backgroundColor = 'transparent';

  userStore.loginUser(payload)
}


// 비밀번호 가시성 토글
const togglePasswordVisibility = () => {
  const passwordInput = document.getElementById('password');
  const passwordType = passwordInput.type === 'password' ? 'text' : 'password';
  passwordInput.type = passwordType;
};


</script>

<style scoped>
.container {
  color: violet;
  font-weight: bolder;
  width: 400px;

  background-color: rgba(79, 50, 103, 0.6);
  border-radius: 50px;
  padding: 50px;

}

/* 로그인 글씨 두께 */
.text-center h2{
  font-weight: 600;
}

/* 로그인 버튼 색상 */
.custom-btn {
  background-color: #E384FF;
  border-color: #E384FF;
}

.custom-btn:hover {
  background-color: #865DFF;
  border-color: #865DFF;
}





</style>
