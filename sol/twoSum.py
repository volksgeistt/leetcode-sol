class Solution(object):
    def twoSum(self, nums, target):
        nmap = {}

        for i, num in enumerate(nums):
            complement = target - num  
            if complement in nmap:
                return [nmap[complement], i]
            nmap[num] = i
        return []

def test():
    solution = Solution()
    cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6)
    ]

    for nums, target in cases:
        final = solution.twoSum(nums, target)
        print("Input -- nums = {}, target = {}".format(nums, target))
        print("Output -- {}".format(final))
        print("")

if __name__ == "__main__":
    test()

# https://leetcode.com/problems/two-sum/
