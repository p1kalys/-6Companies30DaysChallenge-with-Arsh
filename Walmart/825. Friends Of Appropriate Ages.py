class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ans = 0
        count = [0] * 121  # Initialize an array to count the occurrences of each age

        # Count the occurrences of each age
        for age in ages:
            count[age] += 1

        # Calculate friend requests for ages greater than or equal to 15
        for i in range(15, 121):
            ans += count[i] * (count[i] - 1)

        # Calculate friend requests for ages in the range (i // 2 + 8, i)
        for i in range(15, 121):
            for j in range(i // 2 + 8, i):
                ans += count[i] * count[j]

        return ans
