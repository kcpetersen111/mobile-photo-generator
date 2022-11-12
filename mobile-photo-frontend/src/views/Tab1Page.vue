<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <img v-bind:src="imageUrl">
      <ion-item>
        <ion-label>Input:</ion-label>
        <ion-input type="text" placeholder="type something here..." v-model="input" v-on:keydown.enter="sendInput()"></ion-input>
        <ion-button shape="round" @click="sendInput()">GO!</ion-button>
      </ion-item>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { IonInput, IonPage, IonContent } from '@ionic/vue';
// import ExploreContainer from '@/components/ExploreContainer.vue';

export default defineComponent({
  name: 'Tab1Page',
  components: {IonContent, IonPage, IonInput },
  methods: {
    sendInput: async function() {
      // alert(this.imageUrl)
      let response = await fetch("http://code.binary141.com:6969/" + this.size + "/" + encodeURIComponent(this.input), {
        method: 'GET',
        headers: {},
      })
      let data = await response.json()
          this.imageUrl = data["data"];
       
    }
  },
  data(){
    return{
      input: '',
      imageUrl: '',
      size: 1
    }
  }
});
</script>
