class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            s_word = ''.join(sorted(word))

            if s_word in hashmap:
                hashmap[s_word].append(word)
            else:
                hashmap[s_word] = [word]

        super_list = []

        for value in hashmap.values():
            super_list.append(value)

        return super_list

        