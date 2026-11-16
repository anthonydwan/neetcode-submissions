class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        top, bot = 0, R - 1

        while top <= bot:
            vert = (top + bot)//2
            row = matrix[vert]
            if target < row[0]:
                bot = vert-1
            elif target > row[C-1]:
                top = vert+1
            else:
                break

        if not (top <= bot):
            return False

        
        l,r = 0, C-1
        while l <= r:
            mid = (l+r)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid -1
            else:
                l = mid +1
        
        return False