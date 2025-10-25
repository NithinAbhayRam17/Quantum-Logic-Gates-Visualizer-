# Quantum Logic Gates Visualizer (Qiskit 1.x Compatible)
# Author: Siobhan

from qiskit import QuantumCircuit
from qiskit_aer import Aer, AerSimulator
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# --- Function to simulate and visualize a gate ---
def visualize_gate(gate_name):
    qc = QuantumCircuit(1)

    if gate_name == "X":
        qc.x(0)
    elif gate_name == "Y":
        qc.y(0)
    elif gate_name == "Z":
        qc.z(0)
    elif gate_name == "H":
        qc.h(0)
    elif gate_name == "S":
        qc.s(0)
    elif gate_name == "T":
        qc.t(0)
    else:
        print("Invalid gate!")
        return

    qc.measure_all(add_bits=True)
    qc.draw(output='mpl')
    plt.show()

    # Get statevector
    qc_no_measure = qc.remove_final_measurements(inplace=False)
    sv = Statevector.from_instruction(qc_no_measure)
    print(f"\nStatevector for {gate_name} gate:\n", sv)

    # Plot Bloch sphere
    plot_bloch_multivector(sv)
    plt.show()

    # Simulate measurements
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)

    # Plot histogram
    plot_histogram(counts)
    plt.title(f"Measurement results for {gate_name} gate")
    plt.show()


# --- Main Program ---
print("Quantum Logic Gates Visualizer")
print("Available gates: X, Y, Z, H, S, T\n")

gate = input("Enter the gate you want to visualize: ").upper()
visualize_gate(gate)