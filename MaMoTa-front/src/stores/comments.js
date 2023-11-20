// import axios from 'axios'
// import { defineStore } from 'pinia'
// import { useArticleStore } from './article.js'
// import { useAuthStore } from './auth.js'

// export const useCommentStore = defineStore('comment', () => {
//   const token = useAuthStore().token
//   const articleStore = useArticleStore()
//   const commentCreate = function (pk, content) {
//     axios({
//       method: 'post',
//       url: `http://127.0.0.1:8000/community/article/${pk}/comments/`,
//       data: {
//         content
//       },
//       headers: {
//         Authorization: `Token ${token}`
//       }
//     })
//     .then(res => articleStore.detailPost.data.comment_set.push(res.data))
//     .catch(err => console.log(err))
//   }

//   const commentDelete = function(articlePk, commentPk) {
//     axios({
//       method: 'delete',
//       url: `http://127.0.0.1:8000/community/article/${articlePk}/comments/${commentPk}/`,
//       headers: {
//         Authorization: `Token ${token}`
//       }
//     })
//     .then(res => {
//       articleStore.detailArticle.data.comment_set = articleStore.detailArticle.data.comment_set.filter((comment) => {
//         return comment.id != commentPk
//       })
//     })
//   }
//   return { commentCreate, commentDelete}
// }, { persist: true }
// )
