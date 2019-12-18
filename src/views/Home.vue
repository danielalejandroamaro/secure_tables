<template>
  <v-container>
    <v-row justify="center">
      <v-col        
        cols="10"
        md="8"
        >

            <secure_table
            v-for="(table,index) in tables"
            :key="index"            
            :table_name="table"
            :table_rules="table_rules(table)"
            ></secure_table>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
import secure_table from '@/components/secure_table.vue'

export default {
  name: 'home',
  components: {   
    secure_table
  },

  data(){
    return{
      tables:'',
      rules:[]
    }
  },

  methods:{
    table_rules(table_name){
      return this.rules.filter(table => table.table_name == table_name)
    }
  },

  created(){
    this.tables = this.$mokeServices.getTables();
    this.rules = this.$mokeServices.getDefinitions();    
    console.log(Object.keys(this.rules[0]));    
  }

}
</script>
