class Solution {
public:
    // TC->O(n) as covering all nodes of a tree
    // SC->O(1)
    class info{
        public: 
        int maxi;
        int mini;
        bool isBST;
        int sum;
    };

    info solve(TreeNode* root, int &ans){
        // base case
        if(root==NULL)return {INT_MIN, INT_MAX, true, 0};

        info left=solve(root->left, ans);    //checking for eft subtree
        info right=solve(root->right, ans);   // checking for right subtree

        info currNode;

        currNode.sum=left.sum + right.sum + root->val; // updating sum of valid bst nodes
        currNode.maxi=max(root->val, right.maxi);  // updating min and max value at that node
        currNode.mini=min(root->val, left.mini);

        if(left.isBST && right.isBST && (root->val > left.maxi && root->val < right.mini)){
            currNode.isBST=true;  //checking conditions for valid bst
        }
        else{
            currNode.isBST=false;
        }
        // answer update max sum
        if(currNode.isBST)ans=max(ans, currNode.sum);
        return currNode;
    }
    int maxSumBST(TreeNode* root) {
        int maxsum=0;
        info temp=solve(root,maxsum);
        return maxsum;
    }
};
