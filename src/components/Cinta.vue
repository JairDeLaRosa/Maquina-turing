<template>
    <div class="wrapper" ref="wrapper">
      <div class="word" :style="{ transform: `translateX(${position}px)` }">
        <div
          v-for="(letter, index) in word"
          :key="index"
          class="tape"
        >
          {{ letter }}
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name:'cinta-compenet',
    data() {
      return {
        position: 0,
        movements: ["R", "R", "R", "R", "R", "R", "R", "L", "L", "L", "L", "L","L","L", "S"],
        word: "Ejemplo",
        currentIndex: 0,
        intervalId: null,
      };
    },
    mounted() {
      this.moveTape();
    },
    methods: {
      moveTape() {
        this.intervalId = setInterval(() => {
          if (this.movements && this.currentIndex < this.movements.length) {
            const move = this.movements[this.currentIndex];
  
            switch (move) {
              case "R":
                this.position += 50;
                break;
              case "L":
                this.position -= 50;
                break;
              case "S":
                clearInterval(this.intervalId);
                break;
              default:
                break;
            }
  
            this.currentIndex++;
  
            if (this.currentIndex === this.movements.length) {
              clearInterval(this.intervalId);
            }
          } else {
            clearInterval(this.intervalId); // Detiene el intervalo si no hay más movimientos
          }
        }, 500);
      },
    },
  };
  </script>
  
  <style>
  body {
    margin: 0;
    overflow: hidden;
  }
  
  .wrapper {
    width: 100%;
    height: 50px;
    overflow: hidden;
    position: relative;
  }
  
  .word {
    display: flex;
    transition: transform 0.5s ease-in-out;
  }
  
  .tape {
    width: 50px;
    height: 50px;
    background-color: #e74c3c;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.2em;
  }
  </style>
  