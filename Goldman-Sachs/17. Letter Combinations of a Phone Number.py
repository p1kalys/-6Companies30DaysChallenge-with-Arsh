class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        if len(digits)==0:
            return res
        def f(start, val):
            if len(val)==len(digits):
                res.append(val)
                return
            for i in keys[digits[start]]:
                f(start+1,val+i)

        f(0,"")
        return res
