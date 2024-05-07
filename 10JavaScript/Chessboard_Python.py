size = int(input("What size should the chessboard be?"))

for i in range(size):
    row = ''
    for j in range(size):
        row += '#' if (i + j) % 2 == 0 else ' '
    print(row)