namespace QuantumVisualization {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Diagnostics;

    operation QuantumEntanglementDemo() : Result {
        use qubits = Qubit[2];
        {
            H(qubits[0]);    // Put first qubit in superposition
            CNOT(qubits[0], qubits[1]);  // Entangle the qubits

            let results = [MResetZ(qubits[0]), MResetZ(qubits[1])];
            return results[0]; // Both will have the same outcome due to entanglement
        }
    }

    operation WaveInterferenceDemo() : Unit {
        use q = Qubit(); 
        {
            H(q);    // Superposition creates wave interference effects
            let result = MResetZ(q);
            Message($"Wave Interference: Measured state is {result}");
        }
    }

    @EntryPoint()
    operation RunQuantumExperiments() : Unit {
        let entanglementResult = QuantumEntanglementDemo();
        Message($"Entanglement Result: {entanglementResult}");

        WaveInterferenceDemo();
    }
}
