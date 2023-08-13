class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(nums):
            result = target - num
            if result in num_dict:
                return [num_dict[result], i]
            num_dict[num] = i
        return None
nums = []
num_count = int(input("Enter the number of elements: "))

for _ in range(num_count):
    num = int(input("Enter a number: "))
    nums.append(num)

target = int(input("Enter the target number: "))

solution = Solution()
result = solution.twoSum(nums, target)
print(result)
    


            