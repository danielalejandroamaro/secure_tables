<template>
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

    <v-card-text class="pb-0">
      <v-container>
        <v-row>
          <v-col cols="12" class="d-flex flex-row">
            <v-text-field class="mr-2" disabled :value="editedRule.table_name" label="Table Name"></v-text-field>
            <v-select
                style="width: 40px"
                label="Methods"
                cache-items
                required
                :items="methods"
                v-model="editedRule.method"
            ></v-select>
          </v-col>
          <v-col cols="6">
            <div v-for="group of groups_list" :key="group" class="d-flex flex-row align-center" style="margin: auto">
              <v-checkbox v-model="groups" :value="group" :multiple="true">
                {{group}}
              </v-checkbox>
              <span class="flex-grow-1">  {{group}}</span>
            </div>
          </v-col>
          <v-col cols="6">
            <div v-for="group of groups_list" :key="group" class="d-flex flex-row align-center" style="margin: auto">
              <v-checkbox v-model="groups_available" :value="group" :multiple="true">
                {{group}}
              </v-checkbox>
              <span class="flex-grow-1">deactivated</span>
            </div>
          </v-col>
<!--          <v-col>-->
<!--            <v-switch label="Active"-->
<!--                      dnese-->
<!--                      v-model="editedRule.is_active"-->
<!--                      :value="editedRule.is_active"-->
<!--                      :color="editedRule.is_active ? 'success' : 'gray'"-->
<!--            ></v-switch>-->
<!--          </v-col>-->
        </v-row>
      </v-container>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="primary" text @click="close">Cancel</v-btn>
      <v-btn color="primary" text @click="save">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
  export default {
    name: 'edit-dialog',
    props: {
      close: {},
      editedRule: {},
      formTitle: {},
      groups_list: {},
      methods: {},
      save: {}
    },
    data() {
      return {
        groups: [],
        groups_available: [],
      };
    }
  }
</script>
<style>
  * {
    /*-webkit-user-select: none;*/
    /*-moz-user-select: none;*/
    /*-ms-user-select: none;*/
    user-select: none
  }
</style>