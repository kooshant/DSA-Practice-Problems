class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1="qwertyuiopQWERTYUIOP"
        s2="asdfghjklASDFGHJKL"
        s3="zxcvbnmZXCVBNM"
        cnt1,cnt2,cnt3=0,0,0
        valid=True
        res=[]
        for word in words:
            cnt1,cnt2,cnt3=0,0,0
            valid=True
            for i in range(len(word)):
                if word[i] in s1:
                    cnt1+=1
                elif word[i] in s2:
                    cnt2+=1
                else:
                    cnt3+=1
                if cnt1!=i+1 and cnt2!=i+1 and cnt3!=i+1:
                    valid=False
                    break            
            if(valid):
                res.append(word)
        return res
