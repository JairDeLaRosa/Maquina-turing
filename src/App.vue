<template>
  <b-container fluid id="app">
    <b-col>
      <hello-world class="header" :msj="'Machine of turing'" />
    </b-col>

    <b-col class="container-main">
      <cytoscape
        class="cytoscape_style"
        ref="cyRef"
        :config="config"
        :preConfig="preConfig"
        :afterCreated="afterCreated"
      />
      <div class="ml-3">
        <cinta/>
        <div style="border: solid 1px black" class="p-2 mb-2">
          <label class="font-weight-bold" for="demo-sb">Velocidad</label>
          <b-form-spinbutton
            id="demo-sb"
            v-model="value"
            min="100"
            max="1000"
            step="100"
          ></b-form-spinbutton>
        </div>
        <input-world
          @sendResult="onStartSimulation"
          style="border: solid 1px black"
          class="p-2"
        ></input-world>
      </div>
    </b-col>
  </b-container>
</template>

<script>
import COSEBilkent from "cytoscape-cose-bilkent";
import helloWorld from "@/components/HeaderComponents.vue";
import inputWorld from "@/components/InputPalabra.vue";
import cinta from '@/components/Cinta.vue'
export default {
  components: {
    helloWorld,
    inputWorld,
    cinta
  },
  data: () => ({
    value: 500,
    elements: [
      { data: { id: "q0", label: "q0" } },
      { data: { id: "q1", label: "q1" } },
      { data: { id: "q2", label: "q2" } },
      { data: { id: "q3", label: "q3" } },

      {
        data: { id: "e0", source: "q0", target: "q0", label: "a ; a , R" },
      },
      {
        data: { id: "e1", source: "q1", target: "q1", label: "b ; a , R " },
      },
      {
        data: { id: "e2", source: "q1", target: "q1", label: "a ; a , R " },
      },
      {
        data: { id: "e3", source: "q2", target: "q2", label: "a ; a , L " },
      },

      {
        data: { id: "e4", source: "q0", target: "q1", label: "b ; a , R" },
      },
      {
        data: { id: "e5", source: "q1", target: "q2", label: "( ) ; ( ) , L" },
      },
      {
        data: { id: "e6", source: "q2", target: "q3", label: "( ) ; ( ) , S" },
      },
      {
        data: { id: "e4", source: "q0", target: "q1", label: "b ; a , R" },
      },
    ],
    config: {
      style: [
        {
          selector: "node",
          style: {
            "background-color": "#fff",
            color: "white",
            label: "data(id)",
          },
        },
        {
          selector: "edge",
          style: {
            width: 3,
            "line-color": "green",
            color: "white",
            "curve-style": "bezier", // Usar 'bezier' para las flechas
            "target-arrow-shape": "triangle",
            label: "data(label)",
            "text-rotation": "-0.5",
          },
        },
      ],
      layout: {
        animate: true,
        animationDuration: 500,
        animationEasing: undefined,
        name: "grid",
        rows: 1,
      },
    },
  }),
  methods: {
    preConfig(Cytoscape) {
      Cytoscape.use(COSEBilkent);
    },
    afterCreated(cy) {
      // this.cy.push(cy)
      cy.add(this.elements)
        .layout({
          name: "grid",
          rows: 1,
          spacingFactor: 1.5,
        })
        .run();
    },
    onStartSimulation(estados, i) {
      if (i > estados.length - 1) {
        // Fin de la simulación
        console.log("Fin de la simulación");
        return;
      }

      const estado = estados[i];
      const init = estado[0];
      const fin = estado[1];

      // Restablecer el color de todos los nodos a blanco
      this.$refs.cyRef.instance.nodes().style({ "background-color": "white" });

      // Cambiar el color del nodo inicial a azul
      this.$refs.cyRef.instance
        .$(`#${init}`)
        .style({ "background-color": "blue" });

      // Esperar un tiempo antes de cambiar el color del nodo inicial
      setTimeout(() => {
        this.$refs.cyRef.instance
          .$(`#${init}`)
          .style({ "background-color": "white" });

        // Cambiar el color del nodo final a rojo
        this.$refs.cyRef.instance
          .$(`#${fin}`)
          .style({ "background-color": "green" });

        // Esperar un tiempo antes de cambiar el color del nodo final
        setTimeout(() => {
          this.$refs.cyRef.instance
            .$(`#${fin}`)
            .style({ "background-color": "white" });

          // Llamar recursivamente para el siguiente estado
          this.onStartSimulation(estados, i + 1);
        }, 1000);
      }, 1000);
    },
  },
  mounted() {},
};
</script>

<style>
.cytoscape_style {
  width: 50%;
  height: 40%;
  background-color: black;
  border-radius: 5px;
}

.header {
  height: 60px;
  border-radius: 5px;
  margin-bottom: 2px;
}
.container-main {
  display: flex;
}
</style>
