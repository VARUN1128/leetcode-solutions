class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []

        while matrix:
            # 1. Add the first row
            ret += matrix.pop(0)
            
            # 2. Add the last element of each remaining row
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
    
            # 3. Add the last row in reverse order
            if matrix:
                ret += matrix.pop()[::-1]
    
            # 4. Add the first element of each remaining row in reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
    
        return ret
