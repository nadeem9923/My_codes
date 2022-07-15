# Python program to multiply two matrices using a list

A = [[12, 7, 3],
     [0, 5, 6],
     [8, 8, 9]]
B = [[5, 8, 1, 2, ],
     [0, 0, 0, 0],
     [4, 5, 9, 1]]

# multiply matrix
res = [[sum(a * b for a, b in zip(A_row, B_col))
        for B_col in zip(*B)] for A_row in A]
for r in res:
   print(r)