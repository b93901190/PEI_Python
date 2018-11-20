
import collections

WHITE, BLACK = range(2)

Pos = collections.namedtuple('Pos', ('x', 'y'))

def searchMaze(maze, start, end):

    def searchHelp(cur):
        if not (0 <= cur.x < len(maze) and 0 <= cur.y <=len(maze[cur.x]) and maze[cur.x][cur.y]==WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK

        if cur == end:
            return True

        if any(map(searchHelp, (Pos(cur.x-1, cur.y), Pos(cur.x+1, cur.y), Pos(cur.x, cur.y+1), Pos(cur.x, cur.y-1)))):
            return True

        del path[-1]
        return False

    path = []

    if not searchHelp(s):
        return []

    return path


