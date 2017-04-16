maze = [[0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 9]
]
from tabulate import tabulate
width = len(maze)
height = len(maze[0])
print ('Maze width: %s, height %s' % (width, height))


# noinspection PyGlobalUndefined
def move(x, y):
    global FoundWayOut
    FoundWayOut = False
    if FoundWayOut:
        return

    print(tabulate(maze))

    if x < 0 or x > width - 1 or y < 0 or y > height - 1:
        print('Out of bounds'); return
    if maze[x][y] == 9:
        FoundWayOut = True
        print('Got it!'); return
    if maze[x][y] == 1:
        print('That is wall'); return
    if maze[x][y] == 2:
        print('Was here before'); return
    maze[x][y] = 2

    move(x + 1, y) # East
    move(x, y + 1) # South
    move(x - 1, y) # West
    move(x, y - 1) # North

move(0, 0)
if not FoundWayOut:
    print('There is no way out of this!')