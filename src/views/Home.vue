<template>
  <v-container>
    <v-row justify="center">
      <v-col        
        cols="10"
        md="8"
        >
        <stock title="Stock of fruits">         
          <fruits_list/>
          <p class="caption grey--text">Made by Yoe on December 2019</p>          
        </stock>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
import stock from '@/components/stock.vue'
import fruits_list from "@/components/fruits_list.vue"

export default {
  name: 'home',
  components: {
    stock,    
    fruits_list
  }
}
</script>
