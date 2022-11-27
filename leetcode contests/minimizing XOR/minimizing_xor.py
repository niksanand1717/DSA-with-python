class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        bnum1 = bin(num1)[2:]
        bnum2 = bin(num2)[2:]
        mini = 0
        res = []
        l1 = len(bnum1)
        l2 = len(bnum2)
        length = l1 if l1 > l2 else l2
        
        for i in range(length+1, 0, -1):
            bi = bin(i)[2:]
            if bi.count('1') == bnum2.count('1'):
                mini = i
                res.append(i)
        
        return mini, res

obj1 = Solution()
output, results = obj1.minimizeXor(25, 72)
print(results)
print(output)