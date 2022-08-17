class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # st = "lath"
        # print(''.join(sorted(st)))
        dic = {}
        dicIndex = 0
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) not in dic:
                dic[''.join(sorted(strs[i]))] = [strs[i]]
            else:
                dic[''.join(sorted(strs[i]))].append(strs[i])
        return dic.values()