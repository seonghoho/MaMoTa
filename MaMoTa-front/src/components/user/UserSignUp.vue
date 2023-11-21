<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="text-center mb-4">회원가입</h2>
        <div class="mb-3">
          <label for="username" class="form-label">유저네임</label>
          <input
            v-model="username"
            type="username"
            class="form-control"
            id="username"
            placeholder="이름?"
          />
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">이메일</label>
          <input
            v-model="email"
            type="email"
            class="form-control"
            id="email"
            placeholder="name@example.com"
          />
        </div>
        <div class="mb-4">
          <label for="password1" class="form-label">비밀번호</label>
          <input
            v-model="password1"
            type="password"
            class="form-control"
            id="password1"
            placeholder="비밀번호"
          />
        </div>
        <div class="mb-4">
          <label for="password2" class="form-label">비밀번호 확인</label>
          <input
            v-model="password2"
            @keyup.enter="signUp"
            type="password"
            class="form-control"
            id="password2"
            placeholder="비밀번호 확인"
          />
        </div>
        <div class="mb-4">
          <label for="nickname" class="form-label">별명</label>
          <input
            v-model="nickname"
            type="nickname"
            class="form-control"
            id="nickname"
            placeholder="별명"
          />
        </div>
        <div class="mb-4">
          <label for="first_name" class="form-label">성</label>
          <input
            v-model="first_name"
            type="first_name"
            class="form-control"
            id="first_name"
            placeholder="성"
          />
        </div>
        <div class="mb-4">
          <label for="last_name" class="form-label">이름</label>
          <input
            v-model="last_name"
            type="last_name"
            class="form-control"
            id="last_name"
            placeholder="이름"
          />
        </div>
        <div class="d-grid">
          <button @click="signUp" class="btn btn-info mt-4">회원가입</button>
        </div>
      </div>
    </div>
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
const first_name = ref(null)
const last_name = ref(null)

const userStore = useUserStore();


const alertMessage = (msg) => {
  const result = Swal.fire({
    title: `${msg}`,
    icon: "error",
    confirmButtonColor: "#682cd48c",
    confirmButtonText: "확인",
  });
};

const signUp = () => {
  if (!username.value) {
    alertMessage("아이디를 입력해주세요");
    return;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email.value)) {
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
  if (!first_name.value) {
    alertMessage("성을 입력해주세요.");
    return;
  }
  if (!last_name.value) {
    alertMessage("이름을 입력해주세요.");
    return;
  }

  const payload = {
    username: username.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    first_name: first_name.value,
    last_name: last_name.value
  };

  userStore.signUpUser(payload);
};
</script>

<style>
.text-center {
  text-decoration: white;
}
</style>
