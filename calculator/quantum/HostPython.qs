namespace HostPython {
    open Microsoft.Quantum.Intrinsic;
    
    operation Calculate(numbers : Int[]) : Unit {
        Message($"\nQuantum Powers Go! \nCalculating, {numbers}!");
    }
}