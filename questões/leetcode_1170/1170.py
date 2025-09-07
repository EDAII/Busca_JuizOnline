class Solution:
    def numSmallerByFrequency(self, queries, words):
        def f(s):
            return s.count(min(s))
        
        word_frequencies = sorted(f(word) for word in words)
        result = []
        
        for query in queries:
            qf = f(query)
            
            left, right = 0, len(word_frequencies)
            while left < right:
                mid = (left + right) // 2
                if word_frequencies[mid] <= qf:
                    left = mid + 1
                else:
                    right = mid
            
            result.append(len(word_frequencies) - left)
        
        return result

# queries =["bbb","cc"]
# words = ["a","aa","aaa","aaaa"]
# sol = Solution()
# result = sol.numSmallerByFrequency(queries, words)
# print(result)  # retorno esperado: [1,2]