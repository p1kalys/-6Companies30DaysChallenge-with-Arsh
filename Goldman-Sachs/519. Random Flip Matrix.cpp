class Solution {
public:
set<vector<int>> v;
int row,col;
    Solution(int m, int n) {
        row = m;
        col = n;
    }
    
    vector<int> flip() {
        int r = rand() % row;
        int c = rand() % col;
        while (v.count({r,c})) {
            r = rand() % row;
            c = rand() % col;
        }
        v.insert({r,c});
        return {r,c};
    }
    
    void reset() {
        v.clear();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(m, n);
 * vector<int> param_1 = obj->flip();
 * obj->reset();
 */
