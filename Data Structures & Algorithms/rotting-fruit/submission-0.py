from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #some type of bfs to rot the adjacent fruits
        rotted = deque()
        healthy = 0
        minutes = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotted.append((i,j))
                if grid[i][j] == 1:
                    healthy += 1
                else:
                    continue

        if healthy == 0: #means that its all rotted son
            return 0
        
        #iterative bfs
        while rotted and healthy > 0:
            for i in range(len(rotted)):
                r,c = rotted.popleft() #gets the element

                for dr, dc in [(-1, 0), (0, -1), (1,0), (0,1)]: #adjacent elements
                    nr = dr + r
                    nc = dc + c

                    #check bounds & if its able to be rotted
                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        healthy -= 1
                        rotted.append((nr,nc))
            minutes += 1 #after finishing each wave, a new minute gets added


        return minutes if healthy == 0 else -1 # if there are any remaining we must return -1

               