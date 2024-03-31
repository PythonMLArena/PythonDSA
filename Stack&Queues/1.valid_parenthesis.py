# Problem Link : https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

s="(]"
def isValid(s:str):
    st=[]
    k=False
    for i in range(len(s)):
        if s[i]==")":
            if st:
                prev=st.pop()
                if prev!="(":
                    return False  
                else:
                    k=True 
            else:
                return False 
        elif s[i]=="}":
            if st:
                prev=st.pop()
                if prev!="{":
                    return False 
                else:
                    k=True  
            else:
                return False  
        elif s[i]=="]":
            if st:
                prev=st.pop()
                if prev!="[":
                    return False
                else:
                    k=True 
            else:
                return False 
        else:
            st.append(s[i])

    if st:
        return False
    return k

answer=isValid(s)
print(answer)
    
    
        