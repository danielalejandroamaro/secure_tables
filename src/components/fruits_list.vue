<template>

  <!--comienza la tabla-->
  <v-data-table
    :headers="headers"
    :items="fruits"
    :search="search"
    sort-by="id"
  >
    <template v-slot:top>
      
        <v-row>
          <v-col cols="12" sm="9" class="py-0" >
          <v-text-field  
              outlined       
              label="Search a fruit..."
              prepend-inner-icon="mdi-magnify"
              color="primary"
              v-model="search"
              dense
              class=""
              clearable
              ></v-text-field>
          </v-col>
          
          <v-col cols="12" sm="3" class="py-0">
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on }">
              <v-btn block color="primary" dark class="mb-2" v-on="on"><v-icon>mdi-fruit-cherries</v-icon> New Fruit</v-btn>
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
                    <v-col cols="8" sm="4">
                      <v-text-field disabled v-model.number="editedFruit.id" label="Id"></v-text-field>
                    </v-col>
                    <v-col cols="12">
                      <v-text-field v-model="editedFruit.name" placeholder="Apple, pear, almond..." label="Name"></v-text-field>
                    </v-col>
                    <v-col cols="12" >
                      <v-text-field v-model.number="editedFruit.quantity" label="Quantity"></v-text-field>
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
          </v-col>
        </v-row>
     
    </template>
    <template v-slot:item.action="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editFruit(item)"
        color="success"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteFruit(item)"
        color="error"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize">Reset</v-btn>
    </template>
  </v-data-table>
</template>

<script>
  export default {
    data: () => ({
      search: '',
      dialog: false,
      headers: [
        {
          text: 'Id',          
          sortable: false,
          value: 'id',
        },
        { text: 'Name', value: 'name' },
        { text: 'Quantity', value: 'quantity' },        
        { text: 'Actions', value: 'action', sortable: false },
      ],
      fruits: [],
      editedIndex: -1,
      editedFruit: {
        id:0,
        name: '',
        quantity: 0
      },
      defaultFruit: {
        id:Date.now(),
        name: '',
        quantity: 0
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Fruit' : 'Edit Fruit ' + this.fruits[this.editedIndex].name
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
    },

    created () {
      this.initialize()     
    },

    methods: {
      async initialize(){
        try{
          const res = await this.axios.get('http://localhost:3000/fruits');
          this.fruits = res.data;
        }
        catch(e){
          console.log('Error Yoe!... ' + e)
        }            
      },

      editFruit (fruit) {
        this.editedIndex = this.fruits.indexOf(fruit) //Se busca el indice de la fruta editada, si no lo encuentra es adicionar
        this.editedFruit = Object.assign({}, fruit) //Se ponen los datos de la fruta a editar
        this.dialog = true //se activa el modal
      },

      async deleteFruit (fruit) {
        const conf = confirm('Are you sure you want to delete this fruit?')
        if(conf){
          try{
            await this.axios.delete('http://localhost:3000/fruits/' + fruit.id);
            console.log("Work is done... " + fruit.name + " deleted!");
            this.initialize()
          }
          catch(e){
            console.log(e);
          }          
        }
      },

      close () {
        this.dialog = false
        setTimeout(() => {          
          this.editedFruit = Object.assign({}, this.defaultFruit);        
          this.editedIndex = -1
        }, 300)
      },

      async save () {
        if (this.editedIndex > -1) { //en caso de que se este editando

          try{
            const id = this.fruits[this.editedIndex].id;
            await this.axios.put('http://localhost:3000/fruits/' + id, this.editedFruit);
            console.log("Task succeed! " + this.editedFruit.name + " edited without problems")
          }
          catch(e){
            e=>console.log(e)
          }
          
        } else { //nuevo, por tanto se le agrega
            try{
              await this.axios.post('http://localhost:3000/fruits',this.editedFruit);
              this.defaultFruit.id = Date.now();
              console.log("Query succed! " + this.editedFruit.name + " added without problems")
            }
            catch(e){
              e=>console.log(e)
            }
          
        }
        this.initialize()
        this.close()        
      },
    },
  }
</script>