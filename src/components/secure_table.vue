<template>
  <v-card class="mb-2">
    <v-app-bar
        dark
        class="primary"
        no-gutter
        elevation="2"
        @click="show = !show"
    >
      <v-toolbar-title>
        <h3>{{table_name}}</h3>
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <!--Aqui comienza el dialogo-->

      <v-dialog v-model="dialog" max-width="400px">
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on" @click="show=!show">
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </template>

        <edit-dialog
            :close="close"
            :edited-rule="editedRule"
            :form-title="formTitle"
            :groups_list="groups_list"
            :methods="methods"
            :save="save"
        />
      </v-dialog>

      <!--Aqui termina el dialogo-->

    </v-app-bar>

    <!--table elements here-->
    <v-card-text v-show='show'>
      <v-data-table
          dense
          :headers="table_headers"
          :items="table_rules"
          sort-by="id"
          @click:row="editRule(item)"
      >
        <template v-slot:item.method="{ item }">
          <method-tag :method="item.method"/>
        </template>

        <template v-slot:item.groups="{ item }">
          <v-chip small color="primary" v-if='!item.groups'>not available</v-chip>
          <span v-else badge>{{item.groups}}</span>
        </template>
        <template v-slot:item.is_active="{ item }">
          <v-switch
              label="Active"
              :value="item.is_active"
              dense
              :color="item.is_active? 'success':''"
              v-model="item.is_active"
          ></v-switch>
        </template>

        <!--        <template v-slot:item.action="{ item }">-->
        <!--          <v-icon-->
        <!--              small-->
        <!--              @click="editRule(item)"-->
        <!--              color="success"-->
        <!--          >-->
        <!--            mdi-pencil-->
        <!--          </v-icon>-->

        <!--        </template>-->

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
  import EditDialog from "./EditDialog";
  import MethodTag from "./MethodTag";

  export default {
    components: {MethodTag, EditDialog},
    props: {
      table_name: String,
      table_rules: Array,
      global_last_id: Number,
      groups_list: Array
    },

    data() {
      return {
        table_headers: [
          {text: 'Method', value: 'method'},
          {text: 'Groups', value: 'groups'},
          {text: 'Active', value: 'is_active'},
          {text: 'Lock', value: 'locked'},
          // {text: 'Action ', value: 'action', sortable: false},
        ],
        methods: ['GET', 'POST', 'PUT', 'DELETE'],
        dialog: false,
        show: false,
        editedIndex: -1,
        editedRule: {
          id: Date.now(),
          table_name: '',
          method: '',
          groups: '',
          is_active: '',
          locked: ''
        },
        defaultRule: {
          id: Date.now(),
          table_name: this.table_name,
          method: '',
          groups: '',
          is_active: '',
          locked: true
        }

      }
    },

    methods: {

      editRule(rule) {
        this.editedIndex = this.table_rules.indexOf(rule) //Se busca el indice de la row editada para poderlo agregar ahi mismo luego
        this.editedRule = Object.assign({}, rule) //Se ponen los datos de la fruta a editar
        this.dialog = true //se activa el modal
      },

      close() {
        this.dialog = false
        setTimeout(() => {
          this.editedRule = Object.assign({}, this.defaultRule);
          this.editedIndex = -1
        }, 300)
      },

      save() {
        if (this.editedIndex > -1 /*si es mayor se esta editando una row*/) {
          this.$emit('edit-rule', this.editedRule);
          this.close()
        } else /*es -1, o sea no se esta editando, se agrega*/ if (!this.ruleExist(this.editedRule)) {//valida que no exista una row igual
          for (let rule of this.table_rules) {
            if (rule.method == this.editedRule.method && this.editedRule.groups && !rule.groups) { //verifica si se esta agregando un method ya existente con group y lo actualiza
              let groups = this.editedRule.groups;
              this.editedRule = rule;
              this.editedRule.groups = groups;
              this.editRule(this.editedRule);
              this.close();
              return;
            } else if (rule.method == this.editedRule.method && !this.editedRule.groups) { //verifica que no se ponga un method existente asociado ya a un grupo en vacio
              this.close();
              alert("There are groups associated to this method, row wasn't saved")
              return;
            }
          }
          this.$emit('add-rule', this.editedRule);
          this.defaultRule.id = Date.now();
          this.close()
        } else alert("Operation fail!... resulting row exist, please try another config")
      },

      toggleRuleKey(rule, key) {
        this.$emit('toggle-rule-key', rule, key)
      },

      //para comprobar si ya existe una row con un metodo y group determinado, retorna el indice de la row si es true, o false caso contrario
      ruleExist(editedRule) {
        for (let rule of this.table_rules) {
          if (rule.method == editedRule.method && rule.groups == editedRule.groups)
            return true
        }
        return false
      }

    },

    computed: {
      formTitle() {
        return this.editedIndex === -1 ? `New Row` : `Edit Row "${this.table_rules[this.editedIndex].method} ${this.table_rules[this.editedIndex].groups}"`
      }
    },

    watch: {
      dialog(val) {
        val || this.close()
      },
    },

    created() {
      this.editedRule = Object.assign({}, this.defaultRule);
    }
  }
</script>

<style>
  * {
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none
  }
</style>
