<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <img v-bind:src="imageUrl">
      <ion-item v-if="!loading">
        <ion-label>Input:</ion-label>
        <ion-input type="text" placeholder="type something here..." v-model="input" v-on:keydown.enter="sendInput()"></ion-input>
        <ion-button shape="round" @click="sendInput()">GO!</ion-button>
      </ion-item>

      <div v-else id="loadingAnimation" style="display:flex; justify-content:center; padding-top: 30px;">
        {{this.loadingText}}
    </div>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { IonInput, IonPage, IonContent, createAnimation } from '@ionic/vue';
import { ref } from 'vue';
// import ExploreContainer from '@/components/ExploreContainer.vue';

export default defineComponent({
  name: 'Tab1Page',
  components: {IonContent, IonPage, IonInput },
  methods: {
    sendInput: async function() {
      // alert(this.imageUrl)
      this.loading = true;
      let response = await fetch("http://code.binary141.com:6969/" + this.size + "/" + encodeURIComponent(this.input), {
        method: 'GET',
        headers: {},
      })
      let data = await response.json()
      this.imageUrl = data["data"];
      this.loading = false; 
    }
  },
  data(){
    return{
      input: '',
      imageUrl: '',
      loading:false,
      size: 1,
      loadingText: "Loading"
      // elementRef: ref(),
    }
  },
  mounted(){
    
    setInterval(async () => { 
       if(this.loadingText.length>9){
          this.loadingText = "Loading"
       } else {
          this.loadingText += "."
       }
      }, 500);

  },
});
</script>
