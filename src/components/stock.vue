<template>
    <v-card>       
        <v-app-bar
        dark
        class="primary"
        no-gutters
        elevation="2"
        >
            <v-toolbar-title>
                <h3>{{title}}</h3>                
            </v-toolbar-title>            

        </v-app-bar>
        <v-container>
            <v-row dense>
                <v-col cols="12">
                    <slot></slot>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script>
export default {
    name:'stock',
    props:{
        title:String
    }
}
</script>
