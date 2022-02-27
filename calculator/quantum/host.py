import qsharp 
from HostPython import Calculate

print("\n\nWelcome to the quantum calculator!\n")
print("Please enter two numbers you would like to Add\n")

s = input()
numbers = list(map(int, s.split()))

print("\nYou enetered " + str(numbers))
print(Calculate .simulate(numbers = numbers))