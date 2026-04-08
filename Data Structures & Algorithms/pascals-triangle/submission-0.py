class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for n in range(numRows):
            row = [1]

            for k in range(1, n+1):
                row.append(row[-1] * (n-k+1)//k)
            res.append(row)
        return res
        