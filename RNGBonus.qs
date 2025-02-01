import Microsoft.Quantum.Convert.*;
import Microsoft.Quantum.Math.*;

operation Main() : Int {
    let min = 10;
    let max = 100;
    Message($"Sampling a random number between {min} and {max}: ");
    
    // Generate random number in the min..max range.
    let result = GenerateRandomNumberInRange(min, max);
    Message($"Generated random number: {result}");
    return result;
}

/// Generates a random number between `min` and `max`.
operation GenerateRandomNumberInRange(min : Int, max : Int) : Int {
    Message($"Generating a random number between {min} and {max}...");
    
    // Determine the number of bits needed to represent `max`.
    let nBits = BitSizeI(max);
    Message($"Number of bits needed to represent {max}: {nBits}");
    
    // Generate `nBits` random bits.
    mutable bits = [];
    for idxBit in 1..nBits {
        let bit = GenerateRandomBit();
        set bits += [bit];
        Message($"Generated bit {idxBit}/{nBits}: {bit}");
    }
    
    let sample = ResultArrayAsInt(bits);
    Message($"Random sample generated from bits: {sample}");
    
    // Adjust the sample to be within the range [min, max].
    let adjustedSample = sample + min;
    Message($"Adjusted sample (sample + min): {adjustedSample}");
    
    // Return random number if it is within the requested range.
    if adjustedSample > max {
        Message($"Adjusted sample {adjustedSample} exceeds max {max}. Regenerating...");
        return GenerateRandomNumberInRange(min, max);
    } else {
        Message($"Adjusted sample {adjustedSample} is within range. Returning...");
        return adjustedSample;
    }
}

operation GenerateRandomBit() : Result {
    Message("Generating a random bit...");
    
    // Allocate a qubit.
    use q = Qubit();
    Message("Allocated a qubit.");
    
    // Set the qubit into superposition of 0 and 1 using the Hadamard operation.
    H(q);
    Message("Applied Hadamard operation to the qubit.");
    
    // Measure the qubit value.
    let result = M(q);
    Message($"Measured the qubit: {result}");
    
    // Reset the qubit to the |0〉 state.
    Reset(q);
    Message("Reset the qubit to |0〉 state.");
    
    // Return the result of the measurement.
    return result;
}