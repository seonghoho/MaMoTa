import { ref } from "vue";
import { defineStore } from "pinia";
import { useRouter } from "vue-router";
import { signUpApi, fetchCurrentUserApi, loginApi } from "../apis/userApi.js";
import Swal from "sweetalert2";

export const useUserStore = defineStore("user", () => {
    const router = useRouter();
    const token = ref('')
    const isLogin = ref(false);
    const userData = ref({
      pk: null,
      username: "",
    });
    
    const profile = ref({});

    const setCurrentUser = (user) => {
      userData.value.pk = user.pk;
      userData.value.username = user.username;
    };
    
    // 회원가입 - 성공
    const signUpUser = (payload) => {
      signUpApi(payload)
      .then((response) => {
        console.log(response)
        console.log(response.status)
        if (response.status == 204) {
          Swal.fire({
            title: "회원가입 완료. \n 로그인 하시겠습니까?",
            icon: "success",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "네",
            cancelButtonText: "아니요",
          }).then((result) => {
            if (result.isConfirmed) {
              router.push({ name: "userLogin" });
            } else {
              router.push({ name: "home" });
            }
          });
        }
      });
    };

    // 로그인 성공
    const loginUser = (payload) => {
      loginApi(payload)
        .then((response) => {
          if (response.data.key) {
            console.log(response)
            token.value = response.data.key;
            isLogin.value = true;
            window.localStorage.setItem("token", token.value);
            fetchCurrentUser();
          } else {
            Swal.fire({
              title: "로그인에 실패했습니다. \n 아이디와 비밀번호를 확인하세요",
              icon: "error",
              confirmButtonColor: "#682cd48c",
              confirmButtonText: "확인",
            });
          }
        })
        .catch(() => {
          Swal.fire({
            title: "로그인에 실패했습니다.\n아이디와 비밀번호를 확인하세요",
            icon: "error",
            confirmButtonColor: "#682cd48c",
            confirmButtonText: "확인",
          });
        });
    };

    const fetchCurrentUser = () => {
      if (isLogin.value) {
        fetchCurrentUserApi(token.value)
          .then((res) => {
            setCurrentUser(res.data);
            window.localStorage.setItem("userPk", res.data.pk);
            router.push({ name: "community" });
          })
          .catch((err) => {
            console.error(err);
          });
      }
    };

    const logout = () => {
      token.value = "";
      isLogin.value = false;
      userData.value = {
        pk: null,
        username: "",
      };
      window.localStorage.removeItem("token");
      window.localStorage.removeItem("userPk");
      router.push({ name: "community" });
    };

    return {
      token,
      isLogin,
      userData,
      profile,
      setCurrentUser,
      signUpUser,
      loginUser,
      fetchCurrentUser,
      logout,
    };
  },
  { persist: true }
);
