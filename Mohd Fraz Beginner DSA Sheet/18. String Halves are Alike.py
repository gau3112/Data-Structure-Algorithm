class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        mid = len(s)//2
        start_1 = 0
        start_2 = mid
        count_1,count_2 = 0,0
        while start_1<mid or start_2<len(s):
            if s[start_1]=='a' or s[start_1]=='e' or s[start_1]=='i' or s[start_1]=='o' or s[start_1]=='u':
                count_1+=1
            if s[start_2]=='a' or s[start_2]=='e' or s[start_2]=='i' or s[start_2]=='o' or s[start_2]=='u':
                count_2+=1
            start_1+=1
            start_2+=1
        return count_1==count_2
