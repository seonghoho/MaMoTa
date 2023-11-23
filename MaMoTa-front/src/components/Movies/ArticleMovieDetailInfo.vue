<template>
    <div>
        <div class="poster-container" :style="`backgroundImage:url('${getImageUrl(movie.backdrop_path)}')`">
            <img :src="getImageUrl(movie.poster_path)" class="card-img-top poster" alt="#">
            <div class="movie-info">
                <h1>{{ movie.title || movie.name }}</h1>
                <div>
                    <p>개봉일 : {{ movie.release_date }}</p>
                    <p>🔥 {{ movie.vote_average }} / 10</p>
                </div>

                <h3>장르</h3>
                <ul>
                    <li v-for="genreId in movie.genres" :key="genreId">
                        {{ getGenreNameById(genreId) }}
                    </li>
                </ul>

                <div>
                    <h3>줄거리</h3>
                    <p>{{ movie.overview }}</p>
                </div>
            </div>
        </div>



        <!-- 버튼 수정중 -->

        <button :class="{ 'btn-outline-info': isPicked, 'btn-info': !isPicked }" class="btn mt-5 mb-5" style="width: 500px"
            @click="addToMyPickList">
            {{ isPicked ? 'Unpick' : 'Pick' }}
        </button>

        <!-- 여기까지 -->


        <div class="separator"></div>
        <RouterLink :to="{ name: 'articleCreate', query: { movie_title: `${movie.title}` } }">
            게시글 작성
        </RouterLink>
        <div class="separator"></div>
    </div>
</template>
  
<script setup>
import { defineProps, ref, onMounted } from 'vue';
import axios from 'axios';
import { RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/movie'








//////////////////// 수정중 ////////////////////

import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/userStore'
import { usePickStore } from '@/stores/pickListStore'
import { useArticleStore } from '@/stores/article'

const router = useRouter()

const userStore = useUserStore()
const pickStore = usePickStore()
const articleStore = useArticleStore()

// onMounted(() => {
//   if (userStore.isLogin) {
//     pickStore.initializePickList()
//   }
//   articleStore.initializeArticles(props.movie.id)
// })

// pick logic
const isPicked = computed(() => {
    if (userStore.isLogin && pickStore.pickList) {
        return pickStore.pickList.some((m) => m.id === props.movie.id)
    } else {
        return false
    }
})

const addToMyPickList = () => {
    if (!userStore.isLogin) {
        const userConfirmation = window.confirm(
            '로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?'
        )
        if (userConfirmation) {
            router.push({ name: 'userLogin' })
        }
        return
    }

    addListMovie(props.movie.id || props.movie.pk)
        .then((response) => {
            pickStore.addPick(props.movie)
        })
        .catch((error) => {
            console.error('Error adding to list', error)
        })
}



//////////////////// 수정중 ////////////////////









const store = useMovieStore();

const props = defineProps(["movie"]);
const movie = props.movie

const getImageUrl = (path) => {
    if (!path) {
        return '/src/assets/Images/img_no_poster.png';
    }
    return `https://image.tmdb.org/t/p/w300${path}`;
}

const getGenreNameById = (genreId) => {
    const foundGenre = store.genre.genres.find(genre => genre.id === genreId);
    return foundGenre ? foundGenre.name : 'Unknown Genre';
}

// const movieArticles = articleStore.movieArticles

// onMounted(() => {
//   articleStore.getMovieArticles(movie.title);
// });

// console.log(movieArticles)

</script>
  
<style>
.poster {
    max-width: 300px;
    max-height: 450px;
}

.detail,
.movie-info,
.h3,
.p {
    color: white !important;
}


.separator {
    border: none;
    border-top: 2px solid rgb(233, 42, 233);
    margin: 20px 0;
}


.movie-info {
    margin-left: 20px;
}

@media (max-width: 1000px) {
    .poster-container {
        flex-direction: column;
    }

    .movie-info {
        margin-left: 0;
        margin-top: 20px;
    }
}
</style>