class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
         
        word_freq = []
        for key in d.keys():
            word_freq.append((-d[key], key))
        word_freq = sorted(word_freq)
        return [x[1] for x in word_freq[:k]]