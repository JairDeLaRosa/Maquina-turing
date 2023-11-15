<template>
  <div class="main">
    <h1>{{ msj }}</h1>
    <div>
      <!-- <select  v-model="lan" name="language" id="">
        <option value="es">español</option>
        <option value="en">ingles</option>
        <option value="value3"></option>
      </select> -->
    </div>
  </div>
</template>
<script>
export default {
  name: "helloWorld",
  props: {
    msj: String,
  },
  data: () => ({
    lan: "",
  }),
};
</script>

<style>
.main {
  text-align: center  ;
  background: gray;
  
}
.main h1 {
  margin: 2px;
}
</style>
