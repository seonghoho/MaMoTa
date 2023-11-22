import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMusicStore = defineStore('music', () => {
 
  const audios = [
    'src/assets/audios/Homura(炎)-LiSA.mp3',
    'src/assets/audios/Cant Take My Eyes off You.mp3',
    'src/assets/audios/See You Again.mp3',
    'src/assets/audios/Rewrite The Stars.mp3',
  ];

  return { audios }
},{ persist: true })
