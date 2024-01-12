

def find_exit(maze, start):
    """
    Trouve la sortie d'un labyrinthe en utilisant la recherche de profondeur.
    """
    rows, cols = len(maze), len(maze[0])

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or maze[row][col] == 1 or visited[row][col]:
            return False

        visited[row][col] = True

        if maze[row][col] == 9:  
            return True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            if dfs(row + dr, col + dc):
                return True

        return False

    visited = [[False] * cols for _ in range(rows)]
    exit_found = dfs(start[0], start[1])

    if exit_found:
        return start
    else:
        return None

