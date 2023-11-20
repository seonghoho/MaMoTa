// 게시글 전체 디테일 함수 작성 완료

import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('post', () => {
  const articleList = ref([])                     
  const getArticleList = async function () {
    try {
      const res = await axios.get('http://127.0.0.1:8000/community/');
      articleList.value = res.data;
    } catch (err) {
      console.log(err);
    }
  }

  const detailArticle = ref([])
  
  const getDetailArticle = function (pk) {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/article/${pk}`
    })
    .then(res => detailArticle.value = res.data)
    .catch(err => console.log(err))
  }

  const createArticle = function ({rate, title, content, movie}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/community/article/',
      data: {
        rate,
        title,
        content,
        movie
      },

      // headers: { 토큰관련
      //   Authorization: `Token ${token}`
      // }
    })
    // .then(res => router.push({name: 'detail', params:{pk:res.data.id}})) 그 해당글로 바로가게
  }

  // const updatePost = function ({pk, category, title, content}) {
  //   axios({
  //     method: 'put',
  //     url: `http://127.0.0.1:8000/api/v1/posts/${pk}/`,
  //     data: {
  //       category,
  //       title,
  //       content
  //     },
  //     headers: {
  //       Authorization: `Token ${token}`
  //     }
  //   })
  //   .then(res => router.push({name: 'detail', params:{pk:res.data.id}}))
  // }

  // const deletePost = function (pk) {
  //   axios({
  //     method: 'delete',
  //     url: `http://127.0.0.1:8000/api/v1/posts/${pk}/`,
  //     headers: {
  //       Authorization: `Token ${token}`
  //     }
  //   })
  //   .then(res => router.push({name:'posts'}))
  // }
  // const updateArticle = function ({pk, rate, title, content, movie}) {
  //   axios({
  //     method: 'put',
  //     url: `http://127.0.0.1:8000/api/v1/posts/${pk}/`,
  //     data: {
  //       rate,
  //       title,
  //       content,
  //       movie
  //     },
  //     // headers: {
  //     //   Authorization: `Token ${token}`
  //     // }
  //   })
  //   .then(res => router.push({name: 'detail', params:{pk:res.data.id}}))
  // }
  // const deletePost = function (pk) {
  //   axios({
  //     method: 'delete',
  //     url: `http://127.0.0.1:8000/api/v1/posts/${pk}/`,
  //     headers: {
  //       Authorization: `Token ${token}`
  //     }
  //   })
  //   .then(res => router.push({name:'posts'}))
  // }




  return { articleList, getArticleList, detailArticle, getDetailArticle, createArticle}
})