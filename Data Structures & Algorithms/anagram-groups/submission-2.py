class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #this maps the key values to a list

        for s in strs:
            count = [0] * 26 #give a number value to a-z

            for c in s:
                count[ord(c) - ord('a')] +=1
            
            result[tuple(count)].append(s)
        return list(result.values())
