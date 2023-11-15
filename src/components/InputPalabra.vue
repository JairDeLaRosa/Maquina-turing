<template>
  <div>
    <b-container class="w-100">
      <b-row>
        <label style="font-weight: bold">ingrese su palabra:</label>
      </b-row>
      <b-row class="mb-1">
        <b-form-input
          id="input-live"
          v-model="worldValidate"
          :state="worldValidate != '' ? true : false"
          aria-describedby="input-live-help input-live-feedback"
          placeholder="Enter your word"
          trim
        ></b-form-input>
      </b-row>
      <b-row class="mb-1">
        <b-button @click="validateWord" variant="success">verificar</b-button>
      </b-row>
    </b-container>
    <b-container>
      <cinta-compenet ref="cinta"/>
    </b-container>
  </div>
</template>

<script>
import cintaCompenet from './Cinta.vue'
export default {
  components: {cintaCompenet},
  data() {
    return {
      dismissSecs: 3,
      dismissCountDown: 0,
      worldValidate: "",
    };
  },

  methods: {
    async validateWord() {
      let i = 0;
      if (this.worldValidate != "") {
        let resultTransiciones = null;
        let mov = null;
        let palabra=''
        
        await fetch(`http://127.0.0.1:4000/transitions/${this.worldValidate}`, {
          mode: "cors",
          credentials: "include",
        })
          .then((response) => {
            response.json().then((res) => {
              console.log(res)
              resultTransiciones = res.transiciones;
              mov = res.cinta
              palabra=res.palabra
            });
          })
          .catch((e) => {
            console.log(e);
          });

        setTimeout(() => {
          this.$emit("sendResult", resultTransiciones, i);
          this.$refs.cinta.$emit('movimiento', mov, this.worldValidate,palabra)
          }, 1000);
      }
      return
    },
  },
};
</script>

<style></style>
