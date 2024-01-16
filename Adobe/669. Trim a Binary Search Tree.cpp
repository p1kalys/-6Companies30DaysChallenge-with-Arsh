/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* highBalance(TreeNode* root, int high) {
        if (root == NULL) return root;
        if (root-> val > high){
            TreeNode* temp = highBalance(root->left, high);
            return temp;
        }
        else if (root->val < high){
            root->right = highBalance(root->right, high);
            return root;
        }
        else{
            root->right = NULL;
            return root;
        }
    }
    TreeNode* lowBalance(TreeNode* root, int low) {
        if (root == NULL) return root;
        if (root-> val > low){
            root->left = lowBalance(root->left, low);
            return root;
        }
        else if (root->val < low){
            TreeNode* temp = lowBalance(root->right, low);
            return temp;
        }
        else{
            root->left = NULL;
            return root;
        }
    }
    TreeNode* trimBST(TreeNode* root, int low, int high) {
        root = lowBalance(root,low);
        root = highBalance(root, high);
        return root;
    }
};
