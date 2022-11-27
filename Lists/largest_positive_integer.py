class Solution:
    def findMaxK(self, nums):
        ssarr = sorted(nums)
        front = 0
        end = len(nums) - 1
        print(ssarr)
        while front < end:
            if ssarr[end] == ssarr[front]:
                print("Almost over")
                return ssarr[end]
            elif abs(ssarr[front]) < ssarr[end]:
                end -= 1
                print("ELIF")

            else:
                front += 1
                print("ELSE")
                
        return '-1'

if __name__ == "__main__":
    obj = Solution()
    print(obj.findMaxK([1,2,-3,3]))