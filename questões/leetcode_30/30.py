from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = Counter(words)
        n = len(s)
        res = []

        for offset in range(word_len):
            left = right = offset
            seen = {}
            count = 0
            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                    if count == len(words):
                        res.append(left)
                else: 
                    seen.clear()
                    count = 0
                    left = right
        return res

# s = "barfoothefoobarman"
# words = ["foo","bar"]
# sol = Solution()
# result = sol.findSubstring(s, words)
# print(result)  # retorno esperado: [0,9]