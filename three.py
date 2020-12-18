

maze = open('three.csv').read().split('\n')

rows, cols = len(maze), len(maze[0])


def tree_hits(maze, right=3, down=1):

    row, col = 0, 0

    hits = 0

    while row < rows:

        # ignore blank lines
        if maze[row]:
        
            if maze[row][col] == '#':
                hits += 1

        row += down
        col += right
        if col >= cols:
            col -= cols

    return hits


data = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2))

result = 1

for (right, down) in data:
    hits = tree_hits(maze, right, down)

    print(hits)
    
    result *= hits

print(result)
