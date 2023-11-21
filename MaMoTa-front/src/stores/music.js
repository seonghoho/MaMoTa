import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMusicStore = defineStore('music', () => {
 
  const videos = [
    'https://www.youtube.com/embed/iObGpqXKBdY',
    'https://www.youtube.com/embed/6jCRqC5PJ7I',
    'https://www.youtube.com/embed/WwNvVQhsd6I',
  ];

  return { videos }
},{ persist: true })
