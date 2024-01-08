class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        for (int i=0; i<n; i++){
            if (nums[i]%2==0){
                nums[i]=0;
            }
            else{
                nums[i]=1;
            }
        }
        int count = 0;
        int prefix = 0;
        unordered_map<int, int>mp;
        for(int i=0; i<n; i++){
            prefix+=nums[i];
            if(prefix==k){
                count++;
            }
            int rem = prefix-k;
            if (mp.find(rem)!=mp.end()){
                count+=mp[rem];
            }
            mp[prefix]++;
        }
        return count;
    }
};
