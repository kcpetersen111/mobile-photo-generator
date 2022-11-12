<!--- <template>
   <ion-page>
     <ion-header>
       <ion-toolbar>
         <ion-title>Gallery</ion-title>
       </ion-toolbar>
     </ion-header>
     <ion-content :fullscreen="true">
       <ion-header collapse="condense">
         <ion-toolbar>
           <ion-title size="large">Gallery</ion-title>
         </ion-toolbar>
       </ion-header>

       <ExploreContainer name="Image Gallery" />
     </ion-content>
   </ion-page>
 </template> --->


<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <img @src="imageUrl">
      <div v-for="(image) in imageArray" style="display: block; display: flex; justify-content: center;" :key="image">
            <img v-bind:src="image" :key="image">
      </div>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { IonPage, IonContent } from '@ionic/vue';
// import ExploreContainer from '@/components/ExploreContainer.vue';

export default defineComponent({
  name: 'Tab2Page',
  components: { IonContent, IonPage },
  mounted: async function(){
      console.log("This was autoloaded!");
      let response = await fetch("http://code.binary141.com:6969/ListImages/", {
          method: "GET",
          headers: {},
      })

      let data = await response.json()
          this.imageLength = data["images"].split(",").length
          this.imageArray = data["images"].split(",")
      // .then(function (response) {
      //   response.json().then( function (data) {
      //       this.imageLength = data["images"].split(",").length
      //       console.log("Data: ", this.imageLength);
      //   });
      // });
  },
  methods: {
    getImages: function() {
      fetch("/ListImages").then(function (data) {
          console.log("images?: ", data);
      })
    }
  },
  data(){
    return{
      input: '',
      imageUrl: '',
      imageLength: 0,
      imageArray: [],
      size: 1
    }
  }

});
</script>
