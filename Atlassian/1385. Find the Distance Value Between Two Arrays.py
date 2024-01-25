class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()  # Sorting arr2 for binary search
        count = 0

        for num1 in arr1:
            # Using binary search to check if there's a number in arr2 within distance d of num1
            l, r = 0, len(arr2) - 1
            while l <= r:
                mid = (l + r) // 2
                if abs(arr2[mid] - num1) <= d:
                    break
                elif arr2[mid] < num1:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # Else clause executes only if break was not hit, indicating no number within distance d was found
                count += 1

        return count
