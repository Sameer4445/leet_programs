class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        arr=[0]
        for i in s:
            if i=='(':
                arr.append(0)
            else:
                x=arr.pop()
                if x==0:
                    score=1
                else:
                    score=2* x
                arr[-1]+=score

        return arr[0]