class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                tempV, tempInd = stack.pop()
                res[tempInd] = index - tempInd
            else:
                stack.append([temp,index])
        
        return res
            
