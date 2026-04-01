class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {

        unordered_map<int, int>remain;
        remain[0] = -1;
        int sum = 0;
        for(int i = 0; i<nums.size(); ++i){
            sum+=nums[i];
            int remainder = sum%k;

            if(remain.find(remainder) != remain.end()){
                if(i - remain[remainder] >=2)return true;
            }else{
                remain[remainder] = i;
            }

        }

        return false;
};