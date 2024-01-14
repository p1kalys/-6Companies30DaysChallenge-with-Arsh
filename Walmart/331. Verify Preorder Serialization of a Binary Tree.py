class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        n = len(preorder)
        if n == 1 and preorder[0]=='#':
            return True
        if preorder[0]=='#':
            return False
        
        store = []

        i=0

        while i<n:
            s=""
            while i<n and preorder[i]!=",":
                s+=preorder[i]
                i+=1
            store.append(s)
            i+=1

        i = 0

        num = 0
        hashc = 0

        while i < len(store):
            if store[i]!='#':
                num+=1
                if num <= hashc:
                    return False
            else:
                if num < hashc:
                    return False
                else:
                    hashc += 1
            i+=1
        if num+1 != hashc:
            return False
        return True
