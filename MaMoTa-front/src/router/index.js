import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/Comunities/CommunityView.vue'
import PopularMovieView from '@/views/Movies/PopularMovieView.vue'
import TopRatedMovieView from '@/views/Movies/TopRatedMovieView.vue'
import NowPlayingView from '@/views/Movies/NowPlayingView.vue'
import UpComingView from '@/views/Movies/UpComingView.vue'
import MovieDetailView from '@/views/Movies/MovieDetailView.vue'
import ArticleDetailView from '@/views/Comunities/ArticleDetailView.vue'

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
  ]
})

export default router
