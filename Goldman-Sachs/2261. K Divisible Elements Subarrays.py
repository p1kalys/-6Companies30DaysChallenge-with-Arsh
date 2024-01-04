class Solution {
public:
    int countDistinct(vector<int>& nums, int k, int p) {
        map<vector<int>, int>mp;
        for(int i=0; i<nums.size(); i++){
            vector<int> temp;
            for(int j=i; j<nums.size(); j++){
                temp.push_back(nums[j]);
                mp[temp]++;
            }
        }
        int res = 0;
        for (auto i: mp){
            int count = 0;
            for(int j: i.first){
                if (j%p==0){
                    count++;
                }
            }
            if (count <=k){
                res++;
            }
        }
        return res;
    }
};
