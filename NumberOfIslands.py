dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
def count_distinct_islands(grid):
    def dfs(x0, y0, i, j, v):
        nonlocal grid
        rows, cols = len(grid), len(grid[0])
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] <= 0:
            return
        grid[i][j] *= -1
        v.append((i-x0, j-y0))
        
        for k in range(4):
            dfs(x0, y0, i+dirs[k][0], j+dirs[k][1], v)
            
    rows, cols = len(grid), len(grid[0])
    coordinates = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 1:
                continue
            v = []
            dfs(i, j, i, j, v)
            coordinates.add(tuple(v))
    return len(coordinates)

if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = [ list(map(int, input().split())) for _ in range(n) ]
    ans = count_distinct_islands(grid)
    print(ans)
    
