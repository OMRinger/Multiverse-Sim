
from qiskit import QuantumCircuit, execute, Aer

def simulate_entanglement():
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(circuit, simulator).result()
    counts = result.get_counts()
    return counts

def simulate_superposition():
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(circuit, simulator).result()
    counts = result.get_counts()
    return counts
