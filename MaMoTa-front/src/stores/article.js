// 게시글 전체 디테일 함수 작성 완료

import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
// 토큰 부분 임포트 추가
import { useUserStore } from'./userStore'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('post', () => {
  // 토큰 불러오기 추가
  const router = useRouter()
  const token = useUserStore().token
  const articleList = ref([])                     
  // const getArticleList = async function () {
  //   try {
  //     const res = await axios.get('http://127.0.0.1:8000/community/');
  //     articleList.value = res.data;
  //   } catch (err) {
  //     console.log(err);
  //   }
  // }
  //  전체 조회 토큰 부분 추가
  const getArticleList = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/community/',
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then(res => articleList.value = res.data)
    .catch(err => console.log(err))
  }

  const detailArticle = ref([])
  // 디테일 확인 헤더 토큰 부분 추가
  const getDetailArticle = function (pk) {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/article/${pk}`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then(res => detailArticle.value = res.data)
    .catch(err => console.log(err))
  }

  const createArticle = function ({rate, title, content, movie,view_count, movie_title}) {
    console.log(`${token}`)
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/community/article/',
      data: {
        rate,
        title,
        content,
        movie,
        view_count,
        movie_title,

      },
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then(res => router.push({name: 'detail', params:{pk:res.data.id}}))
    .catch(err => console.log(err))
  }

  const updateArticle = function ({pk, rate, title, content, movie,view_count}) {
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/community/article/${pk}/`,
      data: {
            rate,
            title,
            content,
            movie,
            view_count
      },
      headers: {
        Authorization: `Token ${token}`
      }
    })
    // .then(res => router.push({name: 'detail', params:{pk:res.data.id}}))
    .then(res => console.log(`${res}`))

  }

  const deleteArticle = function (pk) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/community/article/${pk}/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then(res => router.push({name:'community'}))
  }
  

  const likeArticle = function(pk){
    axios({
      method: 'get',
      url:`http://127.0.0.1:8000/community/${pk}/like/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
    // .then(res =>{console.log(res)} )
    .then(getArticleList() )


    

  }

  const movieArticles = ref([]);

  const getMovieArticles = (movie_title) => {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/community/',
    })
      .then((res) => {
        // movieArticles.value = res.data.filter(item => item.movie_title === movie_title);
      })
      .catch((err) => {
        console.log(err);
      });
  }

  return { articleList, getArticleList, detailArticle, getDetailArticle, createArticle,updateArticle, deleteArticle, likeArticle, movieArticles, getMovieArticles}
})