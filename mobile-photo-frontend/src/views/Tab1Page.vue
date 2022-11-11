<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <img @src="imageUrl">
      <ion-item>
        <ion-label>Input:</ion-label>
        <ion-input type="text" placeholder="type something here..." v-model="input"></ion-input>
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
    sendInput: function() {
      fetch(this.input).then(function (data) {
        this.imageUrl = data;
      })
    }
  },
  data(){
    return{
      input: '',
      imageUrl: '',
    }
  }
});
</script>
