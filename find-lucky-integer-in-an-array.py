"""Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2."""
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = -1

        for i in range(len(arr)):
            current = arr[i]
            counts = 0

            for j in range(len(arr)):
                if current == arr[j]:
                    counts +=1
            if counts == current:
                lucky = max(lucky,current)
        return lucky 


if __name__ == "__main__":
    arr = [2, 2, 3, 4]
    obj = Solution()
    res = obj.findLucky(arr)
    print(res)

        
    
