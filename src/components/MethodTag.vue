<template>
  <div style="padding: .25em;width: 75px;text-align: center;border-radius: 3px"
       :style="{color:'white' ,background:`${color}`}">{{method}}
  </div>
</template>
<script>
  export default {
    props: {
      method: {}
    },
    name: 'method-tag',
    computed: {
      color() {
        switch (this.method) {
          case 'GET':
            return 'green';
          case 'DELETE':
            return 'red';
          case 'PUT':
            return 'orange';
          case 'POST':
            return 'blue';
        }
        return 'black';
      }
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