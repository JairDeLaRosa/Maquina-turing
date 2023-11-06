class TuringMachine:
    def __init__(self, states, alphabet, tape_symbols, blank_symbol, initial_state, final_state, transitions):
        self.states = states
        self.alphabet = alphabet
        self.tape_symbols = tape_symbols
        self.blank_symbol = blank_symbol
        self.initial_state = initial_state
        self.current_state = initial_state
        self.final_state = final_state
        self.transitions = transitions
        self.tape = []
        self.head = 0
        self.trace = []  # Lista para almacenar las transiciones realizadas en la cinta

    def transition(self, tape_symbol):
        if tape_symbol not in self.tape_symbols:
            raise Exception("Símbolo inválido en la cinta")

        if (self.current_state, tape_symbol) not in self.transitions:
            raise Exception("Transición no definida para el estado actual y el símbolo en la cinta")

        new_state, write_symbol, move_direction = self.transitions[(self.current_state, tape_symbol)]

        # Registro de la transición en la cinta
        self.trace.append((self.current_state, tape_symbol, new_state, write_symbol, move_direction))

        self.tape[self.head] = write_symbol
        if move_direction == 'R':
            self.head += 1
            if self.head == len(self.tape):
                self.tape.append(self.blank_symbol)
        elif move_direction == 'L':
            self.head -= 1
            if self.head < 0:
                self.tape.insert(0, self.blank_symbol)

        self.current_state = new_state

    def run(self, input_string):
        self.tape = list(input_string)
        self.tape.append(self.blank_symbol)  # Agrega un símbolo en blanco al final
        self.head = 0
        self.current_state = self.initial_state
        self.trace = []  # Reinicia el registro de transiciones

        while self.current_state != self.final_state:
            tape_symbol = self.tape[self.head]
            self.transition(tape_symbol)

        return ''.join(self.tape).rstrip(self.blank_symbol), self.trace

# Resto del código igual que en el ejemplo anterior
states = {'q0', 'q1', 'q2', 'q3'}
alphabet = {'a', 'b'}
tape_symbols = {'a', 'b', '_'}
blank_symbol = '_'
initial_state = 'q0'
final_state = 'q3'

# Definir las transiciones de la Máquina de Turing
transitions = {
    ('q0', 'a'): ('q0', 'a', 'R'),
    ('q0', 'b'): ('q1', 'a', 'R'),
    ('q1', 'a'): ('q1', 'a', 'R'),
    ('q1', 'b'): ('q1', 'a', 'R'),
    ('q1', '_'): ('q2', '_', 'L'),
    ('q2', 'a'): ('q2', 'a', 'L'),
    ('q2', 'b'): ('q2', 'b', 'L'),
    ('q2', '_'): ('q3', '_', 'N')  # 'N' significa sin movimiento en este caso
}
# Crear la Máquina de Turing
tm = TuringMachine(states, alphabet, tape_symbols, blank_symbol, initial_state, final_state, transitions)

# Ejecutar la Máquina de Turing con una entrada
input_string = "ababba"
result, transitions_made = tm.run(input_string)
print("Resultado de la Máquina de Turing:", result)
print("Transiciones realizadas en la cinta:")
for transition in transitions_made:
    print(transition)