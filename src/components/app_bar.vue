<template>
    <v-app-bar
      app
      color="blue darken-2"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="@/assets/logo.svg"
          transition="scale-transition"
          width="40"
        />        
      </div>

      <v-spacer></v-spacer>

      <h3>Secure Tables</h3>
    </v-app-bar>
</template>

<script>
export default {
  name:'app_bar'
}
</script>

<style>

</style>
