/* eslint-disable no-unused-vars */
export class TuringMachine {
    constructor(states, alphabet, tapeSymbols, blankSymbol, initialState, finalState, transitions) {
      this.states = states;
      this.alphabet = alphabet;
      this.tapeSymbols = tapeSymbols;
      this.blankSymbol = blankSymbol;
      this.initialState = initialState;
      this.currentState = initialState;
      this.finalState = finalState;
      this.transitions = transitions;
      this.tape = [];
      this.head = 0;
      this.trace = [];
    }
  
    transition(tapeSymbol) {
      if (!this.tapeSymbols.includes(tapeSymbol)) {
        throw new Error("Símbolo inválido en la cinta");
      }
  
      const key = [this.currentState, tapeSymbol];
      if (!this.transitions[key]) {
        throw new Error("Transición no definida para el estado actual y el símbolo en la cinta");
      }
  
      const [newState, writeSymbol, moveDirection] = this.transitions[key];
  
      this.trace.push([this.currentState, tapeSymbol, newState, writeSymbol, moveDirection]);
  
      this.tape[this.head] = writeSymbol;
      if (moveDirection === 'R') {
        this.head += 1;
        if (this.head === this.tape.length) {
          this.tape.push(this.blankSymbol);
        }
      } else if (moveDirection === 'L') {
        this.head -= 1;
        if (this.head < 0) {
          this.tape.unshift(this.blankSymbol);
        }
      }
  
      this.currentState = newState;
    }
  
    run(inputString) {
      this.tape = inputString.split('');
      this.tape.push(this.blankSymbol);
      this.head = 0;
      this.currentState = this.initialState;
      this.trace = [];
  
      while (this.currentState !== this.finalState) {
        const tapeSymbol = this.tape[this.head];
        this.transition(tapeSymbol);
      }
  
      return [this.tape.join('').replace(new RegExp(`${this.blankSymbol}$`), ''), this.trace];
    }
  }
  
 