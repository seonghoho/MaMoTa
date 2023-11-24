<template>
  <div class="container mt-5 signup_form">
    <div class="row justify-content-center signup">
      <div class="col-md-6">
        <h2 class="text-center mb-4 signup_header">회원가입</h2>
        <div class="mb-3">
          <label for="username" class="form-label">이메일</label>
          <input
            v-model="username"
            type="username"
            class="form-control"
            id="username"
            placeholder="MaMoTa@ssafy.com"
            :class="{ 'filled': username }"
          />
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">이메일 확인</label>
          <input
            v-model="email"
            type="email"
            class="form-control"
            id="email"
            placeholder="MaMoTa@ssafy.com"
            :class="{ 'filled': email }"
          />
        </div>
        <div class="mb-4">
          <label for="password1" class="form-label">비밀번호</label>
          <div class="input-group">
            <input
              v-model="password1"
              type="password"
              class="form-control"
              id="password1"
              placeholder="비밀번호"
              :class="{ 'filled': password1 }"
              
            />
            <button class="btn btn-outline-secondary" type="button" @click="togglePasswordVisibility1">
              <i class="bi bi-eye"></i>
            </button>
          </div>
        </div>
        <div class="mb-4">
          <label for="password2" class="form-label">비밀번호 확인</label>
          <div class="input-group">
            <input
              v-model="password2"
              @keyup.enter="signUp"
              type="password"
              class="form-control"
              id="password2"
              placeholder="비밀번호 확인"
              :class="{ 'filled': password2 }"
            />
            <button class="btn btn-outline-secondary" type="button" @click="togglePasswordVisibility2">
              <i class="bi bi-eye"></i>
            </button>
          </div>
        </div>
        <div class="mb-4">
          <label for="nickname" class="form-label">별명</label>
          <input
            v-model="nickname"
            type="nickname"
            class="form-control"
            id="nickname"
            placeholder="별명"
            :class="{ 'filled': nickname }"
          />
        </div>

        <div class="d-grid">
          <button @click="signUp" class="custom-btn btn btn-info mt-4">회원가입</button>
        </div>
        
        </div>
      </div>
      <br><br><br><br><br><br><br><br><br>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/userStore";
import Swal from "sweetalert2";

// 회원 가입
const username = ref(null)
const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const userStore = useUserStore();


const alertMessage = (msg) => {
  const result = Swal.fire({
    title: `${msg}`,
    icon: "error",
    confirmButtonColor: "#E384FF",
    confirmButtonText: " 확인 ",
    padding: "3em",
    background: "rgba(256,256,256,0.9)",
    backdrop: "rgba(0,0,123,0.4) url('/src/assets/Images/nyan_cat.gif')  center top",
  });
};


const signUp = () => {
  if (!username.value) {
    alertMessage("아이디를 입력해주세요");
    return;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email.value)) {
    alertMessage("이메일을 확인해주세요");
    return;
  }  

  if (username.value !== email.value) {
    alertMessage("비밀번호가 일치하지 않습니다");
    return;
  }

  if (!emailRegex.test(username.value)) {
    alertMessage("아이디는 이메일 형식이어야 합니다");
    return;
  }


  if (!password1.value) {
    alertMessage("비밀번호를 입력해주세요");
    return;
  }
  if (password1.value.length < 8) {
    alertMessage("비밀번호가 너무 짧습니다. \n 8자리 이상 입력해주세요.");
    return;
  }

  if (password1.value !== password2.value) {
    alertMessage("비밀번호가 일치하지 않습니다");
    return;
  }

  if (!nickname.value) {
    alertMessage("닉네임을 입력해주세요.");
    return;
  }

  const payload = {
    username: username.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    // first_name: first_name.value,
    // last_name: last_name.value
  };

  // 배경색 변경 코드 추가
  document.getElementById('app').style.backgroundColor = 'transparent';

  userStore.signUpUser(payload);
};



// 비밀번호 가시성 토글
const togglePasswordVisibility1 = () => {
  const passwordInput = document.getElementById('password1');
  const passwordType = passwordInput.type === 'password' ? 'text' : 'password';
  passwordInput.type = passwordType;
};

const togglePasswordVisibility2 = () => {
  const passwordInput = document.getElementById('password2');
  const passwordType = passwordInput.type === 'password' ? 'text' : 'password';
  passwordInput.type = passwordType;
};



</script>

<style>
.signup_header {
  color: violet;
  font-weight: 550;
}

.signup {
  color: violet;
  margin-left: -100px;
  margin-right: -100px;
}

.signup_form {
  background-color: rgba(0, 0, 0, 0.45);
  border-radius: 50px;
  padding-top: 20px;
  width: 700px;
  height: 650px;
}

.text-center {
  text-decoration: white;
}



/* 제출버튼 */
.custom-btn {
  background-color: #E384FF;
  border-color: #E384FF;
}

.custom-btn:hover {
  background-color: #865DFF;
  border-color: #865DFF;
}

.form-control:focus {
  background-color: #FFA3FD;
}



</style>
