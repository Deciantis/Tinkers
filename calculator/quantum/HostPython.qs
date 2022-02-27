namespace HostPython {
    open Microsoft.Quantum.Intrinsic;
    
    operation SayHello(numbers : Int[]) : Unit {
        Message($"\nQuantum Powers Go! \nCalculating, {numbers}!");
    }
}