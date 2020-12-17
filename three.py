

maze = open('three.csv').read().split('\n')

rows, cols = len(maze), len(maze[0])

row, col = 0, 0

hits = 0

while row < rows:
    if data[row][col] = '#':
        hits += 1

    row += 1
    col += 3
    if col >= cols:
        col -= cols

print(hits)[
    
