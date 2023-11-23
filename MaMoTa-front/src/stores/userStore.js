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
      // response가 존재하고, response.status가 존재하며 204인 경우
      if (response && response.status === 204) {
        Swal.fire({
          title: "회원가입 완료. \n 여행을 떠나시겠습니까?",
          icon: "success",
          showCancelButton: true,
          confirmButtonColor: "#810CA8",
          cancelButtonColor: "#FA2FB5",
          confirmButtonText: "네",
          cancelButtonText: "아니요",
          background: '#D1C4E9',
        }).then((result) => {
          if (result.isConfirmed) {
            router.push({ name: "userLogin" });
          } else {
            router.push({ name: "home" });
          }
        });
      }
    })
    .catch((error) => {
      console.error("회원가입 중 에러가 발생했습니다:", error);
      // 여기서 error에 대한 처리를 추가할 수 있습니다.
    });
};


    // 로그인 성공
    const loginUser = (payload) => {
      loginApi(payload)
        .then((response) => {
          if (response.data.key) {
            // console.log(response)
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
              background: '#D1C4E9',
            });
          }
        })
        .catch(() => {
          Swal.fire({
            title: "로그인에 실패했습니다.\n아이디와 비밀번호를 확인하세요",
            icon: "error",
            confirmButtonColor: "#682cd48c",
            confirmButtonText: "확인",
            background: '#D1C4E9',
          });
        });
    };

    const fetchCurrentUser = () => {
      if (isLogin.value) {
        fetchCurrentUserApi(token.value)
          .then((res) => {
            setCurrentUser(res.data);
            window.localStorage.setItem("userPk", res.data.pk);




            // Swal.fire({
            //   title: "로그인된건가?",
            //   icon: "success",
            //   confirmButtonColor: "#682cd48c",
            //   confirmButtonText: "확인",
            // });


            let timerInterval;
            Swal.fire({
              title: "원하는 영화를 찾아 떠나보아요!",
              html: "영화 찾으러 떠나기 <b></b> 초 전..🚀",
              timer: 3000,
              timerProgressBar: true,
              didOpen: () => {
                Swal.showLoading();
                const timer = Swal.getPopup().querySelector("b");
                timerInterval = setInterval(() => {
                  timer.textContent = `${Math.ceil(Swal.getTimerLeft() / 1000)}`;
                }, 100);
              },
              willClose: () => {
                clearInterval(timerInterval);
              }
            }).then((result) => {
              /* Read more about handling dismissals below */
              if (result.dismiss === Swal.DismissReason.timer) {
                console.log("I was closed by the timer");
              }
            });





            router.push({ name: "home" });
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
