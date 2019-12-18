<template>
  <v-container>
    <v-row justify="center">
      <v-col        
        cols="10"
        md="8"
        >

            <secure_table
            v-for="(table,index) in filledTables"
            :key="index"            
            :table_name="table"
            :table_rules="table_rules(table)"
            @delete="deleteRule"
            @toggle-rule-lock="toggleRuleLock"    
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
    initialize() {
      this.tables = this.$mokeServices.getTables();
      this.rules = this.$mokeServices.getDefinitions()   
    },

    table_rules(table_name) {
      return this.rules.filter(table => table.table_name == table_name)
    },

    deleteRule(rule) {
      const ruleIndex = this.rules.indexOf(rule);
      this.rules.splice(ruleIndex,1)
    },

    toggleRuleLock(rule) {      
      const ruleIndex = this.rules.indexOf(rule);
      const ruleValue = this.rules[ruleIndex].locked;
      this.rules[ruleIndex].locked = !ruleValue
    }
  },

  computed:{
    //para saber si la tabla tiene elementos, en caso contrario no se renderiza
    filledTables(){
      return this.tables.filter(table => this.table_rules(table).length)
    }
  },

  created(){
    this.initialize()
  }

}
</script>
