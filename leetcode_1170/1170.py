import bisect

class Solution:
    def numSmallerByFrequency(self, queries, words):
        def calculate_frequency_of_smallest_character(string): 
            return string.count(min(string))
        
        word_frequencies = sorted(calculate_frequency_of_smallest_character(word) for word in words)
        result = []
        
        for query in queries:
            query_frequency = calculate_frequency_of_smallest_character(query)
            insertion_point = bisect.bisect_right(word_frequencies, query_frequency)
            result.append(len(word_frequencies) - insertion_point)
        
        return result

# queries = ["cbd"]
# words = ["zaaaz"]
# sol = Solution()
# result = sol.numSmallerByFrequency(queries, words)
# print(result)  # Saída esperada: [1]