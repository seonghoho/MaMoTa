// 게시글 전체 디테일 함수 작성 완료

import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('post', () => {
  const articleList = ref([])                     
  const getArticleList = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/community/'
    })
    .then(res => articleList.value = res.data)
    .catch(err => console.log(err))
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

  // const createArticle = function ({category, title, content}) {
  //   axios({
  //     method: 'post',
  //     url: 'http://127.0.0.1:8000/article/',
  //     data: { 
  //       category,
  //       title,
  //       content
  //     }
  //   })

  return { articleList, getArticleList, detailArticle, getDetailArticle}
})