class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # sort the array so the duplicates are next to each other
        nums.sort()

        # get the length and initialize a variable to 0 for the starting index
        length = len(nums)
        i = 0
        # k is the number of unique elements
        k = 0

        # continue to search the array while the index is not the last element
        while i < (length - 1): 
            # if the element at the current index equals to the next element, remove the next element
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
                # the length reduces by 1
                length -= 1
                # stay at the same index, so we do not add to the i
            else:
                # otherwise, move the index to the next element bc it's unique
                i += 1
                k += 1

        print(k)


        