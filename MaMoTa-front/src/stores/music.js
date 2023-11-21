import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMusicStore = defineStore('music', () => {
 
  const videos = [
    'https://www.youtube.com/embed/WwNvVQhsd6I',
    'https://www.youtube.com/embed/iObGpqXKBdY',
  ];

  return { videos }
},{ persist: true })
