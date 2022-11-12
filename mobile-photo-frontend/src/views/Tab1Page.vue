<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div style="display: flex; justify-content: center;">
        <img v-bind:src="imageUrl">
      </div>
      <ion-item style="max-width: 1000px; margin: auto;">
        <ion-label>Input:</ion-label>
        <ion-input type="text" placeholder="type something here..." v-model="input" v-on:keydown.enter="sendInput()"></ion-input>
        <ion-button shape="round" @click="sendInput()">GO!</ion-button>
      </ion-item>
      
      <!-- <ion-item>
        <ion-button shape="round" @click="saveImage()">SAVE!</ion-button>
      </ion-item> -->
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
       
    },

    // saveImage: async function() {
    //     const a = document.createElement("a");
    //     a.href = this.imageUrl;
    //     a.download = "";
    //     document.body.appendChild(a);
    //     a.click();
    //     document.body.removeChild(a);
    // }
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
