from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0: col.append([])
                col[j].append(matrix[i][j])
                print(col)
                print(j, i)

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3],[4,5,6]]
print(Solution().transpose(matrix))