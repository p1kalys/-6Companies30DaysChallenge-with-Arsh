#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        s=n*(n+1)//2
        s1=n*(n+1)*(2*n + 1)//6
        sn=0
        s1n=0
        for i in range(n):
            sn+=arr[i]
            s1n+=(arr[i]**2)
        val1=sn-s
        val2=s1n-s1
        val2=val2//val1
        x=(val1+val2)//2
        y=x-val1
        return [x,y]
        
