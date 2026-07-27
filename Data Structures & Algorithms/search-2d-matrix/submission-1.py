class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start1 = 0
        end1 = len(matrix) - 1


        while start1 <= end1:
            matr = start1 + ((end1 - start1) // 2)
            start2 = 0
            end2 = len(matrix[0]) - 1
            if matrix[matr][start2] == target:
                return True
            if matrix[matr][start2] > target:
                end1 = matr - 1
                continue
            elif matrix[matr][start2] < target:
                if matrix[matr][end2] >= target:
                    while start2 <= end2:
                        ind = start2 + ((end2 - start2) // 2)
                        # print(f"ind: {ind} and {matrix[matr][ind]}")
                        if matrix[matr][ind] > target:
                            end2 = ind - 1
                        elif matrix[matr][ind] < target:
                            start2 = ind + 1
                        else:
                            return True
                    return False
                else:
                    start1 = matr + 1
        return False


