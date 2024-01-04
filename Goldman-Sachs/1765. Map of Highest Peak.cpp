class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        int n = isWater.size();
        if (n == 0) return isWater;
        int m = isWater[0].size();
        if (m == 0) return isWater;
        int max_val = n + m;
        vector<vector<int>> height(n);
        for (int i=0; i<n; i++) {
            vector<int> row(m, 0);
            height[i] = row;
            for (int j=0; j<m; j++) {
                if (isWater[i][j] == 1) continue;
                int above = max_val;
                if (i > 0) above = height[i-1][j];
                int left = max_val;
                if (j > 0) left = height[i][j-1];
                height[i][j] = min(max_val, min(above, left) + 1);
            }
        }
        for (int i=n-1; i>=0; i--) {
            for (int j=m-1; j>=0; j--) {
                if (isWater[i][j] == 1) continue;
                int above = max_val;
                if (i > 0) above = height[i-1][j];
                int left = max_val;
                if (j > 0) left = height[i][j-1];
                int below = max_val;
                if (i < n-1) below = height[i+1][j];
                int right = max_val;
                if (j < m-1) right = height[i][j+1];
                height[i][j] = min(
                    max_val, 
                    min(min(above, below), min(left, right)) + 1);
            }
        }
        return height;
    }
};
