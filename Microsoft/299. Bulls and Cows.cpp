class Solution {
public:
    string getHint(string s, string g) {
        string ans = "";
        int correct = 0;
        unordered_map<char,int>m;
        for(int i=0; i<s.size(); i++){
            if(s[i]==g[i]) correct++;
            else m[s[i]]++;
        }
        ans+=(to_string(correct));
        ans+='A';
        int count = 0;
        for(int i=0; i<g.size(); i++){
            if(s[i]!=g[i]){
                if (m.find(g[i])!=m.end()){
                    count++;
                    m[g[i]]--;
                    if(m[g[i]]==0) m.erase(g[i]);
                }
            }
        }
        ans+=(to_string(count));
        ans+='B';
        return ans;
    }
};
