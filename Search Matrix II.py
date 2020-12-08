from math import floor
from typing import List


class Solution:
    def subMatrix(self, matrix: List[List[int]], left_top: List[int], right_bottom: List[int]) -> List[List[int]]:
        new_matrix = []
        if left_top[0] == right_bottom[0]:
            right_bottom[0] += 1
        if left_top[1] == right_bottom[1]:
            right_bottom[1] += 1
        for i in range(left_top[0], min(right_bottom[0] + 1, len(matrix))):
            row = []
            for j in range(left_top[1] + 1, right_bottom[1]):
                row.append(matrix[i][j])
            if row:
                new_matrix.append(row)
        return new_matrix

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        height = len(matrix)
        width = len(matrix[0])
        if height <= 2 and width <= 2:
            for row in matrix:
                for i in row:
                    if i == target:
                        return True
            return False
        m_y = floor(height / 2)
        m_x = floor(width / 2)
        if matrix[m_y][m_x] == target:
            return True
        elif matrix[m_y][m_x] > target:
            return self.searchMatrix(self.subMatrix(matrix, [0, 0], [m_y, m_x]), target)
        else:
            return self.searchMatrix(self.subMatrix(matrix, [0, m_x], [m_y, width]), target) or self.searchMatrix(self.subMatrix(matrix, [m_y, m_x], [height, width]), target) or self.searchMatrix(self.subMatrix(matrix, [m_y, 0], [height, m_x]), target)


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13,
                                                  14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    print(Solution().subMatrix(matrix, [0, 2], [5]))
    target = 15
    print(Solution().searchMatrix(matrix, target))
