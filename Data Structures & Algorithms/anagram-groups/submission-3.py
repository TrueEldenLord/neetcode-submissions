class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #stores the value of a-z

        for s in strs:
            count = [0] * 26 #we use this to assing a-z a number

            for c in s:
                count[ord(c) - ord("a")] +=1 #makes it so a is 1 and z is 26

            result[tuple(count)].append(s) 
        return list(result.values())