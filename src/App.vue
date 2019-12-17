<template>
  <v-app>

<!-- App navbar -->
    <app_bar/>

<!--Content of routes-->
    <v-content>
      <router-view/>
    </v-content>

  </v-app>
</template>

<script>
import app_bar from './components/app_bar.vue';

export default {
  name: 'App',

  components: {
    app_bar
  },

  data: () => ({
    //
  }),
};
</script>
