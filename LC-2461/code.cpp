class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int>m;
        int l = 0, r = 0;
        long long maxSum = 0;
        long long curSum = 0;
        while(r<nums.size()){
            m[nums[r]]++;
            curSum+=nums[r];
            while(m[nums[r]]>1){
                m[nums[l]]--;
                curSum-=nums[l];
                l++;
            }
            if(r-l+1>k){
                m[nums[l]]--;
                curSum -= nums[l];
                l++;
            }
            if(r-l+1 == k){
                maxSum = max(curSum, maxSum);
            }
            r++;
        }
        return maxSum;
    }
};