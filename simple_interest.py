# Python Program for calculating simple interest. Taking values from user.

print("Enter the Principle Amount: ")
P = int(input())
print("Enter Time Period: ")
N = float(input())
print("Enter Rate of Interest (%): ")
R = float(input())
si = (P*N*R)/100
print("\nSimple Interest Amount: ")
print(si)