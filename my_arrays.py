#8 Find duplicates
some_list = ['a','b','c','b','m','n','n']

duplicates = []
# for value in some_list:
#     if some_list.count(value)>1:
#         if value not in duplicates:
#             duplicates.append(value)

duplicates = [value for value in some_list if some_list.count(value)>1 and value not in duplicates]

print(duplicates)

#9 Create a function that reverses a string:
# "Hi, my name is John!"
#

def reverseStr(string: str):
    # result = []
    # for i in range(len(string)-1, -1, -1):
    #     result.append (string[i])
    # return "".join(result)

    return "".join([string[i] for i in range(len(string)-1, -1, -1)])

    # return string[::-1]

print (reverseStr("Hi, my name is John!"))

#10 Merge sorted arrays
def mergeSortedArrays(a: list, b: list):
    # result = a + b
    # result.sort()
    # return result

    # return sorted(a + b)

    if len(a) == 0: return b
    if len(b) == 0: return a

    result = []
    i,j = 0,0

    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1

    if i == len(a): # add remaining items of array 'b' into the 'result' array
        for v in b[j:]:
            result.append(v)
    else: # add remaining items of array 'a' into the 'result' array
        for v in a[i:]:
            result.append(v)

    return result


a = [0,3,4,31]
b = [4,6,30]
print (a)
print (b)

print (mergeSortedArrays(a, b))


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary = dict()
        for i in range(len(nums)):
            comp = target - nums[i]
            # print(f"comp={comp}, nums[i]={nums[i]}")
            if not comp in dictionary:
                dictionary[nums[i]] = i 
            else:
                j = dictionary[comp]
                return [j, i]
        return []

# nums = [2,7,11,15]
# target = 9

# print()
# sol1=Solution()
# print(sol1.twoSum(nums, target))

# MoveZeroes
# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count, i = 0, 0
        while i<len(nums):
            if nums[i]==0:
                nums.pop(i)
                count+=1
            else:
                i+=1
        zeroes = [0 for i in range(count)]
        nums += zeroes

nums = [0,1,0,3,12]
sol1 = Solution()
sol1.moveZeroes(nums)
# print (nums)

# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maximum = maxarray = nums[0]
        for i in range(1,len(nums)):
            # print (f'-----i = {i}-----')
            # print (f'nums[i] = {nums[i]}, maxarray = {maxarray}')
            maxarray = max(nums[i], maxarray+nums[i])
            # print (f'maxarray = {maxarray}')
            maximum = max(maxarray, maximum)
            # print (f'maximum = {maximum}')
        return maximum

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# sol1 = Solution()
# print ("||||||||||| Maximum Subarray ||||||||")
# print (nums)

# print(sol1.maxSubArray(nums))

# nums = [5,4,-1,7,8]
# sol1 = Solution()
# print(sol1.maxSubArray(nums))

# Rotate array
# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for j in range(k):
        #     nums.append(nums[-1])
        #     for i in range(len(nums)-1, 0, -1):
        #         nums[i] = nums[i-1]
        #     nums[0] = nums[-1]
        #     nums.pop()
        # print(nums)

        # nums = nums[len(nums)-k:] + nums[0:len(nums)-k]

        # for j in range(k):
        #     nums.append(nums[-1])
        #     nums.pop(j)

        new_array = []
        for i in range(k%len(nums)):
            new_array.append(nums[len(nums)-k+i])
        print (new_array)
        for i in range(len(nums)-k%len(nums)):
            new_array.append(nums[i])
        nums = new_array

        print (nums)
        

nums = [1,2,3,4,5,6,7]
k = 3
sol1 = Solution()
print ("|||||||||||ROTATE ARRAY||||||||")
print (nums)
sol1.rotate(nums, k)


# Longest Word
# https://coderbyte.com/editor/Longest%20Word:Python3

def LongestWord(sen):
    count = 0
    maximum = 0
    max_word = word = ''
    for char in sen:
        if char.isalnum():
            count += 1
            word += char
        else:
            if maximum<count:
                max_word = word
                maximum = count
            count = 0
            word = ""
    if maximum<count:
        max_word = word
        maximum = count
    return max_word

# code goes here
    # return sen

sentence = "fun&!! time"

# keep this function call here 
print(LongestWord(sentence))