"""Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4."""



from typing import List

class Solution:
    def Count_max_freq(self,nums:List[int])->int:
        frequency = {}
        for num in nums:
            frequency[num]=frequency.get(num,0)+1
        max_freq = max(frequency.values())
        result = 0
        for freq in frequency.values():
            if freq == max_freq:
                result += freq
        return result
if __name__ == "__main__" :
    arr = [1,2,2,3,1,4]
    obj = Solution()
    res = obj.Count_max_freq(arr)
    print(res)