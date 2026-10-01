class Solution:
    def isValid(self, s: str) -> bool:
        items=[]
        for i in s:
            if (i=="(" or i=="[" or i=="{"):
                items.append(i)
            else:
                if(len(items)==0):
                    return False
                elif(items[-1]=="(" and i==")"):
                    items.pop()
                elif(items[-1]=="[" and i=="]"):
                    items.pop()
                elif(items[-1]=="{" and i=="}"):
                    items.pop()
                else:
                    return False
        return len(items)==0

        

        
        