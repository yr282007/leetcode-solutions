class Solution:
    def isPalindrome(self, x):
        self.x=x
        s=""
        st=str(x)
        o=st
        for i in range(len(st)-1,-1,-1):
            print(i)
            s=s+st[i]
        
        if s==o:
            return True
        else:
            return False




            

