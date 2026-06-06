class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listOfMaps = []
        result = {}

        for i, word in enumerate(strs):
            mapping = {}
            for char in word:
                if char in mapping:
                    mapping[char]+=1
                else:
                    mapping[char] = 1

            if mapping in listOfMaps:
                result[listOfMaps.index(mapping)] += [word]
            else:
                listOfMaps.append(mapping)
                result[len(listOfMaps)-1] = [word]
        
        return list(result.values())
        

        