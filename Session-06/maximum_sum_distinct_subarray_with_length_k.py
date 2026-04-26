class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        current_sum = 0
        count = {}
        left = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1
            
            if right - left + 1 > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                current_sum -= nums[left]
                left += 1
                
            if right - left + 1 == k and len(count) == k:
                res = max(res, current_sum)
        return res
