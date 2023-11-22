import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/Comunities/CommunityView.vue'
import PopularMovieView from '@/views/Movies/PopularMovieView.vue'
import TopRatedMovieView from '@/views/Movies/TopRatedMovieView.vue'
import NowPlayingView from '@/views/Movies/NowPlayingView.vue'
import UpComingView from '@/views/Movies/UpComingView.vue'
import MovieDetailView from '@/views/Movies/MovieDetailView.vue'
import ArticleDetailView from '@/views/Comunities/ArticleDetailView.vue'
import ArticleCreateView from '@/views/Comunities/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/Comunities/ArticleUpdateView.vue'

// 프로필 페이지
import UserInfo from '@/components/user/UserInfo.vue'
import UserPick from '@/components/user/UserPick.vue'
import UserArticle from '@/components/user/UserArticle.vue'
import UserFollower from '@/components/user/UserFollower.vue'




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // 커뮤니티 큰 틀 페이지
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    // 아티클 상세페이지
    {
      path: '/detail/:id',
      name: 'detail',
      component: ArticleDetailView
    },
    // 아티클 생성페이지
    {
      path: '/articleCreate',
      name: 'articleCreate',
      component: ArticleCreateView,
    },
    // 디테일 수정 페이지
    {
      path: '/articleUpdate/:id',
      name: 'articleUpdate',
      component: ArticleUpdateView
    },

    {
      path: '/popular',
      name: 'PopularMovieView',
      component: PopularMovieView
    },
    {
      path: '/toprated',
      name: 'TopRatedMovieView',
      component: TopRatedMovieView
    },
    {
      path: '/nowplaying',
      name: 'NowPlayingView',
      component: NowPlayingView
    },
    {
      path: '/upcoming',
      name: 'UpComingView',
      component: UpComingView
    },

    {
      path: '/:id',
      name: 'movie',
      component: MovieDetailView,
    },
    {
      path: "/search",
      name: "search",
      component: () => import(/* webpackChunkName: "search" */ "@/components/Movies/SearchMovie.vue")
    },
    
    // 로그인, 로그아웃 관련
    {
      path: '/user/signup',
      name: 'userSignup',
      component: () => import('@/views/User/UserSignupView.vue')
    },
    {
      path: '/user/login',
      name: 'userLogin',
      component: () => import('@/views/User/UserLoginView.vue')
    },
    {
      path: '/logout',
      name: 'logout',
      component: () => import('@/views/User/UserLogoutView.vue')
    },

    // 유저 프로필
    {
      path: '/user/profile/:userId',
      name: 'userProfile',
      component: () => import('@/views/User/UserProfileView.vue'),
      beforeEnter: (to, from, next) => {
        const isCurrentUser = to.params.userId === window.localStorage.getItem('userPk')

        if (
          to.path.endsWith('info') ||
          to.path.endsWith('pick') ||
          to.path.endsWith('article') ||
          to.path.endsWith('follower')
        ) {
          next()
          return
        }

        next(
          isCurrentUser
            ? `/user/profile/${to.params.userId}/info`
            : `/user/profile/${to.params.userId}/pick`
        )
      },
      children: [
        { path: 'info', name: 'userInfo', component: UserInfo },
        { path: 'article', name: 'UserArticle', component: UserArticle },
        { path: 'pick', name: 'UserPick', component: UserPick },
        { path: 'follower', name: 'UserFollower', component: UserFollower }
      ]
    },


  ]
})

export default router
