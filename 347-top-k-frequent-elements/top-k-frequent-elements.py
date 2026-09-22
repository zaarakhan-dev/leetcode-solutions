class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        sorted_numbers = sorted(count.keys() , key=lambda n: count[n], reverse = True)

        return sorted_numbers[:k]
        