<template>
  <div>
    <b-container class="w-100">
      <b-row>
        <label style="font-weight: bold">ingrese su palabra:</label>
      </b-row>
      <b-row class="mb-1">
        <b-form-input
          id="input-live"
          v-model="inputString"
          :state="inputString != '' ? true : false"
          aria-describedby="input-live-help input-live-feedback"
          placeholder="Enter your word"
          trim
        ></b-form-input>
      </b-row>
      <b-row class="mb-1">
        <b-button @click="validateWord" variant="success">verificar</b-button>
      </b-row>
      <b-row>
        <b-alert
          :show="dismissCountDown"
          dismissible
          :variant="worldValidate ? 'success' : 'danger'"
        >
          <h3>
            {{ worldValidate ? "es palindromo es " : "no es palindromo" }}
          </h3>
          <P>{{ dismissCountDown }} seconds...</P>
        </b-alert>
      </b-row>

      
    </b-container>
  </div>
</template>

<script>
import { TuringMachine } from "@/assets/Turing.js";
export default {
  components: {
  },
  data() {
    return {
      dismissSecs: 3,
      dismissCountDown: 0,
      inputString: "",
      turing: null,
      worldValidate: "",
      result : ['[q0,q0]','[q0,q1]','[q1,q1]','[q1,q2]','[q2,q2]','[q2,q2]','[q2,q3]']
    };
  },
  mounted() {
    const states = ["q0", "q1", "q2", "q3"];
    const alphabet = ["a", "b"];
    const tapeSymbols = ["a", "b", "_"];
    const blankSymbol = "_";
    const initialState = "q0";
    const finalState = "q3";

    // Definir las transiciones de la Máquina de Turing
    const transitions = {
      q0: ["q0", "a", "R"],
      q0b: ["q1", "a", "R"],
      q1a: ["q1", "a", "R"],
      q1b: ["q1", "a", "R"],
      q1_: ["q2", "_", "L"],
      q2a: ["q2", "a", "L"],
      q2b: ["q2", "b", "L"],
      q2_: ["q3", "_", "N"],
    };

    // Crear la Máquina de Turing

    this.turing = new TuringMachine(
      states,
      alphabet,
      tapeSymbols,
      blankSymbol,
      initialState,
      finalState,
      transitions
    );
  },
  methods: {
    validateWord(){
      let i=0
      let array = [];
      //quitar corchetes
      this.result.forEach((element) => {
       let palabra = element.replace("[", "");
        palabra = palabra.replace("]", "");
        array.push(palabra);
      });
      //volviendo un array de array
      let arryOfArray = [];
      array.forEach((element) => {
        arryOfArray.push(element.split(","));
      });
      this.$emit('sendResult',arryOfArray,i)
      
    }

   
  },
};
</script>

<style></style>
