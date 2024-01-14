class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1

        heap = [(-freq, word) for word, freq in word_count.items()]
        heapq.heapify(heap)

        ans = []
        for _ in range(k):
            freq, word = heapq.heappop(heap)
            ans.append(word)

        return ans
