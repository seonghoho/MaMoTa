<template>
  <div class="content">
    <div class="search-bar">
      <input type="text" placeholder="검색어를 입력하세요." @change="getKeyword">
    </div>
    <section class="sec_search">
      <h2 class="search-word">"{{ searchWord }} " 검색결과</h2>
      <ul>
        <li v-bind:key="key" v-for="(search, key) in searchList">
          <a @click="$store.commit('routerMovieInfo', search[0])">
            <div class="search__thumbnail">
              <img :src="search[1]" alt="포스터" v-if="search[1] !== null">
              <img src="../assets/img_no_poster.png" alt="No-Data" v-if="search[1] === null">
            </div>
            <p class="search__title">{{ search[2] }}</p>
            <p class="search__release">{{ search[3] }}</p>
          </a>
        </li>
      </ul>
      <button
        class="search__button-more"
        @click="getPageMore"
        style="color:white"
        v-show="showBtns"
      >더 불러오기</button>
    </section>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      searchWord: null,
      searchList: [],
      pageNo: 1,
      showBtns: false
    };
  },
  computed: {
    ...mapState(["url", "params", "imgURL"])
  },
  methods: {
    getKeyword(e) {
      this.searchWord = e.target.value;
      this.searchList = [];
      this.getSearchList(this.searchWord);
    },
    getPageMore() {
      this.pageNo++;
      this.getSearchList(this.searchWord, this.pageNo);
    },
    getSearchList(keyword, pageNo) {
      this.axios
        .get(this.url.TMDb + this.url.search, {
          params: {
            api_key: this.params.apiKey,
            language: this.params.langKo,
            query: keyword,
            include_adult: "false",
            page: pageNo
          }
        })
        .then(res => {
          const result = res.data.results;
          result.forEach((data, idx) => {
            this.searchList.push([
              data.id,
              data.poster_path === null
                ? null
                : this.imgURL.poster + data.poster_path,
              data.title,
              data.release_date === "" ? "-" : data.release_date
            ]);
          });
          return result.length;
        })
        .then(length => {
          if (!length) {
            alert("데이터가 없습니다.");
            this.showBtns = false;
          } else this.showBtns = true;
        })
        .catch(err => {
          console.error(err);
        })
        .finally(fin => {});
    }
  }
};
</script>

<style>
.search-bar input{width:98%;  height: 40px; line-height: 50px; border: 0; border-bottom: 1px solid #666; background-color: transparent; padding: 0 1%; font-size: 20px}

.sec_search {min-height: 500px}
.sec_search h2{font-size: 24px; margin: 20px 0 10px}
.sec_search ul{overflow: hidden}
.sec_search ul li{padding-bottom: 20px; float: left; width: 9%; margin: 0 .555%; transition: all .4s}

.sec_search .search__thumbnail{}
.sec_search .search__thumbnail img{width:100%; height: auto;}

.sec_search .search__title, .sec_search .search__release{padding: 0 5px; text-overflow: ellipsis; white-space: nowrap; overflow: hidden}

.search__button-more{width: 100%; text-align: center; line-height: 35px; background: #e002fa; color: #fff}

@media screen and (min-width:1001px){
  .sec_search ul li:nth-child(10n+1){margin-left: 0}
  .sec_search ul li:nth-child(10n){margin-right: 0}
}
@media screen and (max-width:1000px) and (min-width:861px) {
  .sec_search ul li{width:19%; margin: 0 .5% 20px .5%}
  .sec_search ul li:nth-child(5n+1){margin-left: 0}
  .sec_search ul li:nth-child(5n){margin-right: 0}
}

@media screen and (max-width:860px) and (min-width:641px) {
  .sec_search ul li{width:24%;  margin: 0 .5% 20px .5%}
  .sec_search ul li:nth-child(4n+1){margin-left: 0}
  .sec_search ul li:nth-child(4n){margin-right: 0}
}
@media screen and (max-width:640px)  {
  .sec_search ul li{width:49%; margin: 0 .5% 20px .5%}
  .sec_search ul li:nth-child(4n+1){margin-left: 0}
  .sec_search ul li:nth-child(4n){margin-right: 0}
}

.content__upcoming ul li{padding-bottom: 20px; float: left; width: 9%; margin: 0 .555%; transition: all .4s}
.content__upcoming ul li:first-child{margin-left: 0} .content__upcoming ul li:last-child{margin-right: 0}
.content__upcoming ul li a{display: block; width: 100%; height: 100%}
.content__upcoming .upcoming__thumbnail{width: 100%; height: auto; padding-bottom: 5px}
.content__upcoming .upcoming__thumbnail img{width: 100%; height: auto}
.content__upcoming .upcoming__title{text-overflow: ellipsis; white-space: nowrap; overflow: hidden}
.content__upcoming .upcoming__release{font-weight: 100; font-size: 14px}
@media screen and (max-width:860px){
  .content__upcoming ul li{width: 19%}
}
@media screen and (max-width:480px){
  .content__upcoming ul li{width: 48%; margin-right: 1%}
  .content__upcoming ul li:nth-child(2n){margin-left: 1%; margin-right: 0}
}
</style>