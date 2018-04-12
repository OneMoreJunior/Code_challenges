"""
n students divide k apples equally, the remaining residue remains in the basket. How many apples will each student get?
How many apples will remain in the basket?
The program receives the numbers n and k on the input and must output the required number of apples (two numbers).
"""

n = int(input())
k = int(input())

print(k//n)
print(k%n)