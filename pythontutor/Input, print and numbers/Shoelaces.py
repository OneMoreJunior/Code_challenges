"""
The shoe factory is going to start producing an elite model of shoes. Laces for lacing will be arranged in two rows,
the distance between the rows is equal to a, and the distance between the holes in the row b. The number of holes in
each row is N. Lacing must be done in an elite way "up, horizontally in a different row, upward, horizontally, etc."
(see figure). In addition, so that the laces can be tied with an elite bow, the length of the free end of the lace
should be l. What should be the length of the lace for these shoes?
The program receives four natural numbers a, b, l and N on the input - in that order - and must output one number - the
required length of the lace.
"""

a = int(input())
b = int(input())
l = int(input())
N = int(input())

sum = 0
sum += (N+N-1) * a
sum += (N-1) * 2*b
sum += 2*l

print(sum)
