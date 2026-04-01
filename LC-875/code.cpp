#define vl __int128

class Solution {
public:
    bool canEat(vector<int>&piles, int h, int k){
        vl hours = 0;
        for(auto i: piles){
            hours+= ceil((double)i/k);
        }

        return hours<=h;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int end = INT_MIN;
        int st = 1;
        for(auto it: piles){
            if(it>end)end = it;
        }

        int ans = end;
        while(st<=end){
            int mid = st + (end-st)/2;

            if(canEat(piles, h, mid)){
                ans = mid;
                end = mid-1;
            }else{
                st = mid+1;
            }
        }
        return ans;
    }
};