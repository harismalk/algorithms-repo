class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for rowIndex in range(numRows):
            row = [1]
            for colIndex in range(1, rowIndex+1):
                row.append(int(row[-1]*(rowIndex-colIndex+1)//colIndex))
            res.append(row)
        return res

        