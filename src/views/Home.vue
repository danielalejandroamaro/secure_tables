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
            :global_last_id="global_last_id"
            :groups_list="groups_list"  
            @toggle-rule-key="toggleRuleLock"
            @edit-rule="editRule"
            @add-rule="addRule" 
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

    //para togglear los estados lock y active
    toggleRuleLock(rule, rule_key) {           
      const ruleIndex = this.rules.indexOf(rule);
      const ruleValue = this.rules[ruleIndex][rule_key];
      this.rules[ruleIndex][rule_key] = !ruleValue;      
    },

    editRule(editedIndex,editedRule){
      Object.assign(this.rules[editedIndex], editedRule)
    },

    addRule(newRule){
      this.rules.push(newRule)
    }

  },

  computed:{
    //para saber si la tabla tiene elementos, en caso contrario no se renderiza
    filledTables(){
      return this.tables.filter(table => this.table_rules(table).length)
    },

    global_last_id(){
      return this.rules[this.rules.length-1].id
    },

    //para computar los roles existentes en las tablas y adicinarlos al select del adicionar
    groups_list(){
      let groups = [];
      this.rules.forEach( function(el){ 
        if(groups.indexOf(el.groups) == -1){
          groups.push(el.groups);
        } 
      });      
      return groups
    }
  },

  created(){
    this.initialize();    
  }

}
</script>
