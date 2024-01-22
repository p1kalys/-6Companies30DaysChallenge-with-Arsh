class Solution {
public:
    int maximizeSquareHoleArea(int n, int m, vector<int>& h, vector<int>& v) {
        int m1=0,m2=0;
        int c=1;
        sort(h.begin(),h.end());
        sort(v.begin(),v.end());
        for(int i=1;i<h.size();i++){
            if(h[i-1]+1==h[i]){
                c++;
            }
            else{
                c=1;
            }
            m1=max(m1,c);
        }
        c=1;
        for(int i=1;i<v.size();i++){
            if(v[i-1]+1==v[i]){
                c++;
            }
            else{
                c=1;
            }
            m2=max(m2,c);
        }
        if(h.size()==1 || v.size()==1) return 4;  
        int l=min(m1+1,m2+1);
        return l*l;

    }
};
