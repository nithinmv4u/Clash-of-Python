from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = []
        for i in range(len(grid)):
            row = []
            onesRow = 0
            zerosRow = 0
            for j in range(len(grid[i])):
                row.append(0)
                if grid[i][j] == 1:
                    onesRow += 1
                else: zerosRow += 1
            differance = onesRow - zerosRow
            # diff.append(row)
            diff.append([differance for j in range(len(grid[i]))])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    diff[i][j] +=1
                else: diff[i][j] -= 1
                
        print(diff)


grid = [[0,1,1],[1,0,1],[0,0,1]]
Solution().onesMinusZeros(grid)