import qsharp 
from HostPython import SayHello

print("\n\nWelcome to the quantum calculator!\n")
print("Please enter two numbers you would like to Add\n")

s = input()
numbers = list(map(int, s.split()))

print("These are the numbers you enetered " + str(numbers))
print(SayHello.simulate(numbers = numbers))