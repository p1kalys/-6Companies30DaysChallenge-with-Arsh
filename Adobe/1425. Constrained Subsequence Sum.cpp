class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int>dp(n);
        priority_queue<pair<int, int>>pq;

        pq.push({0, -1});
        for(int i=0;i<n;i++){
            while(!pq.empty()){
                if(pq.top().second == -1 || pq.top().second >= i-k)
                    break;
                else if(pq.top().second < i-k)
                    pq.pop();
            }

            int val = pq.top().first;
            dp[i] = nums[i] + val;
            pq.push({dp[i], i});
        }

        int res = INT_MIN;
        for(int i=0;i<n;i++){
            res = max(res, dp[i]);
        }

        return res;
    }
};
