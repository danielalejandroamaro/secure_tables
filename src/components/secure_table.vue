<template>
    <v-card class="mb-2">
        <v-app-bar
        dark
        class="primary"
        no-gutter
        elevation="2"
        >
            <v-toolbar-title>
                <h3>{{table_name}}</h3>                
            </v-toolbar-title>

            <v-spacer></v-spacer>
            
            <!--Aqui comienza el dialogo-->

            <v-dialog v-model="dialog" max-width="500px">
                
            <template v-slot:activator="{ on }">
              <v-btn icon v-on="on">
                <v-icon>mdi-plus</v-icon>
            </v-btn>
            </template>

            <v-card>
              <v-app-bar
              dark
              class="primary"
              no-gutters
              elevation="2">
                <v-card-title>
                  <span class="headline">{{ formTitle }}</span>
                </v-card-title>                
              </v-app-bar>              

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="3" sm="2">
                      <v-text-field disabled v-model.number="editedRule.id" label="Id"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="10">
                      <v-text-field disabled :value="editedRule.table_name" label="Table Name"></v-text-field>
                    </v-col>
                    <v-col cols="6" sm="4">
                        <v-select
                            label="Methods"
                            cache-items                           
                            required
                            :items="methods"
                            v-model="editedRule.method"
                         ></v-select>
                    </v-col>
                    <v-col cols="6" sm="8">
                        <v-select
                           label="Groups"
                           cache-items                           
                           required
                           :items="groups_list"
                           v-model="editedRule.groups"
                       ></v-select>
                    </v-col>       
                    <v-col cols="12" >
                      <v-text-field v-model="editedRule.is_active" label="Active"></v-text-field>
                    </v-col>      
                    <v-col cols="12" >
                      <v-text-field v-model="editedRule.locked" label="Locked"></v-text-field>
                    </v-col>    
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" text @click="close">Cancel</v-btn>
                <v-btn color="primary" text @click="save">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>

            <!--Aqui termina el dialogo-->           

        </v-app-bar>

        <!--table elements here-->
        <v-card-text>
            <v-data-table
            :headers="table_headers"
            :items="table_rules"   
            sort-by="id"
            >    

                <template v-slot:item.is_active="{ item }">                    
                    <v-icon            
                    small
                    :class="['mdi', item.is_active? 'mdi-checkbox-marked':'mdi-checkbox-blank-outline']"                    
                    :color="item.is_active? 'success':'gray'"
                    @click="toggleRuleKey(item, 'is_active')"
                    >                    
                    </v-icon>                   
                </template>

                <template v-slot:item.action="{ item }">
                  <v-icon
                    small                    
                    @click="editRule(item)"
                    color="success"
                  >
                    mdi-pencil
                  </v-icon>
                  
                </template>

                <template v-slot:item.locked="{ item }">
                    <v-icon                    
                    small
                    :class="['mdi', item.locked? 'mdi-lock':'mdi-lock-open-variant']"                    
                    :color="item.locked? 'error':'success'"                    
                    >                    
                    </v-icon>
                </template>

                <template v-slot:no-data>
                  <v-btn color="primary">Reset</v-btn>
                </template>

            </v-data-table>
        </v-card-text>

    </v-card>
</template>

<script>
export default {
    props: {
        table_name:String,
        table_rules: Array,
        global_last_id: Number,
        groups_list: Array
    },

    data() {
        return {
            table_headers:[
                { text: 'Method', value: 'method' },
                { text: 'Groups', value: 'groups' },
                { text: 'Active', value: 'is_active' },
                { text: 'Lock', value: 'locked' },
                { text: 'Action ', value: 'action', sortable: false },
            ],
            nextId: this.global_last_id,
            methods:['GET','POST','PUT','DELETE'],
            dialog: false,
            editedIndex:-1,
            editedRule:{
                id:'',
                table_name:'',
                method:'',
                groups:'',
                is_active:'',
                locked:''
            },
            defaultRule:{
                id: this.nextId++,
                table_name:this.table_name,
                method:'',
                groups:'Not Available',
                is_active:'',
                locked:''
            }          

        }
    },

    methods: {
        
        addRule() {
            alert('Add Rule works')
        },

        editRule(rule) {
            this.editedIndex = this.table_rules.indexOf(rule) //Se busca el indice de la row editada para poderlo agregar ahi mismo luego
            this.editedRule = Object.assign({}, rule) //Se ponen los datos de la fruta a editar
            this.dialog = true //se activa el modal
        },

        close(){
            this.dialog = false
            setTimeout(() => {          
                this.editedRule = Object.assign({}, this.defaultRule);
                this.editedIndex = -1
            }, 300)
        },
        
        save () {
        if (this.editedIndex > -1) { //si es mayor se esta editando una row
            //Object.assign(this.table_rules[this.editedIndex], this.editedRule)
            console.log('editando');
            this.$emit('edit-rule', this.editedIndex, this.editedRule)
          
        } else { //es -1, o sea no se esta editando
            console.log(this.editedRule);
            this.$emit('add-rule', this.editedRule)
        }        
        this.close()
      },

        toggleRuleKey(rule, key){
            this.$emit('toggle-rule-key', rule, key)
        }
       
    },

    computed:{
        formTitle () {
            return this.editedIndex === -1 ? `New Row on "${this.table_name}"` : `Edit Row "${this.table_rules[this.editedIndex].method} ${this.table_rules[this.editedIndex].groups}"`
        }
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
    },

    created(){
        this.editedRule = Object.assign({}, this.defaultRule);
    }
}
</script>

<style>

</style>
