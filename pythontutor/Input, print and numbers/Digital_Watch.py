"""
Given a number n. Since the beginning of the day, n minutes have passed.
Determine how many hours and minutes the electronic clock will display at this time.
The program should output two numbers: the number of hours (from 0 to 23) and the number of minutes (from 0 to 59).
Note that the number n can be greater than the number of minutes in a day.
"""

n = int(input())

x = n//60
print(x%24)
print(n%60)