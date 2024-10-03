class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # get the length of the array
        length = len(nums)
        
        # use i as the current number that we are counting
        i = nums[0]
        # this is the current count of the number i's in the array
        current = 0
        # use j to keep track of the index used for the while loop
        j = 0

        # keep looping while the list is not at its end yet
        while j < length:
            # if the current number is equal to the number we are searching for
            if nums[j] == i:
                # increase the count of that number by 1
                current += 1
                # if the count is greater than 2, then pop the number at that element to decrease the array
                if current > 2:
                    nums.pop(j)
                    # decrease the size of the array -- the index does not need to move
                    length -= 1
                else:
                    # otherwise, move to the next index
                    j += 1
                
            # if the current number is different than our previously searched number
            else:
                # make it our new current number
                i = nums[j]
                # reset all of the stats (the current count would be at 1 since we found the first instance of it)
                current = 1
                # move to the next index
                j += 1

        return length