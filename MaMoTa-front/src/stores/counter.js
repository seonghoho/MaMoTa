// counter.js는 임시용 입니다! 나중에 본인이 원하는 stores를 만들 때
// 참고할만한 스켈레톤 코드입니다!

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
 

  return { count, doubleCount, increment }
},{ persist: true })
