class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #This checks if the string are the same length bc if they are not then the strings cant be anagrams
        if len(s) != len(t):
            return False
        
        #This creates 2 hasmaps to track the # of times a character shows up in the string
        countS, countT = {},{}

        #This is looping through the len of s the reason we dont do
        #len of t aswell is bc both strings are the same lenght
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) #The 0 is a default value if the key doesnt exist yet
            countT[t[i]] = 1 + countT.get(t[i],0) # so we would get 0 + 1 then 1 + 1 then 2 + 1 as the code loops
        
        return countS == countT

