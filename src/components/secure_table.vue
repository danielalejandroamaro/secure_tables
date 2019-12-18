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

            <v-btn icon @click="addRule">
                <v-icon>mdi-plus</v-icon>
            </v-btn>

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
        table_rules: Array
    },

    data() {
        return {
            table_headers:[
                { text: 'Method', value: 'method' },
                { text: 'Groups', value: 'groups' },
                { text: 'Active', value: 'is_active' },
                { text: 'Lock', value: 'locked' },
                { text: 'Action ', value: 'action', sortable: false },
            ]
        }
    },

    methods: {
        
        addRule() {
            alert('Add Rule works')
        },

        editRule(rule) {
            console.log(rule);
        },        

        toggleRuleKey(rule, key){
            this.$emit('toggle-rule-key', rule, key)
        }
       
    }
}
</script>

<style>

</style>
