import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'


// 영화 List 조회 API
export const getMoviesList = (page = 1) => {
  return axios.get(`${API_URL}/movies/?page=${page}`)
}

// 각 영화 상세 조회 API
export const getMovieDetail = (moviePk) => {
  return axios.get(`${API_URL}/movies/${moviePk}/`)
}







// 사용자의 영화 Pick API
export const addListMovie = (moviePk) => {
  const token = window.localStorage.getItem('token')
  // console.log(moviePk)
  // console.log(token)
  return axios
  .post(`${API_URL}/movies/${moviePk}/addlist/`,
    {},
    {
      headers: {
        Authorization: `Token ${token}`
      }
    }
  )
}






// 영화 article List 조회
export const fetchMovieArticles = (moviePk) => {
  return axios
    .get(`${API_URL}/movies/${moviePk}/articles/`)
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 사용자의 영화 평론 작성 API
export const createMovieArticle = (moviePk, payload) => {
  const token = window.localStorage.getItem('token')
  return axios
    .post(`${API_URL}/movies/${moviePk}/articles/`, payload, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 사용자의 영화 평론 삭제 API
export const deleteMovieArticle = (moviePk, articlePk) => {
  const token = window.localStorage.getItem('token')
  return axios
    .delete(`${API_URL}/movies/${moviePk}/articles/${articlePk}`, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 사용자의 영화 평론 수정 API
export const updateMovieArticle = (moviePk, articlePk, payload) => {
  const token = window.localStorage.getItem('token')
  return axios
    .put(`${API_URL}/movies/${moviePk}/articles/${articlePk}/`, payload, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 영화 comment List 조회
export const getCommentList = (moviePk, articlePk) => {
  return axios
    .get(`${API_URL}/movies/${moviePk}/articles/${articlePk}/comments/`)
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 사용자의 comment 작성 API
export const createNewCommentAPI = (moviePk, articlePk, payload) => {
  const token = window.localStorage.getItem('token')
  return axios
    .post(`${API_URL}/movies/${moviePk}/articles/${articlePk}/comments/`, payload, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 사용자의 comment 삭제 API
export const deleteComment = (moviePk, articlePk, commentPk) => {
  const token = window.localStorage.getItem('token')
  return axios
    .delete(`${API_URL}/movies/${moviePk}/articles/${articlePk}/comments/${commentPk}`, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}

// 사용자의 article 좋아요 API
export const likeArticleApi = (moviePk, articlePk) => {
  const token = window.localStorage.getItem('token')
  return axios
    .post(
      `${API_URL}/movies/${moviePk}/articles/${articlePk}/comments/like/`,
      {},
      {
        headers: {
          Authorization: `Token ${token}`
        }
      }
    )
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}
