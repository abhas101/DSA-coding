#Moves all zeroes to the end of the array in-place while maintaining the order of non-zero elements using an optimal O(n) approach.

class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        the idea is to maintain a count variable for non zero elements, and then if i find a zero, we do nothing.
        and if we see a non zero element, we move it to the fornt.
        1,2,3,0,1,0
        1,2,3 will swap with themselves, and when 0 is encountered, the counter will stop there, and when non zero is provided, it will be swapped.
        """
        count = 0
        for i in range(len(nums)):
            # count of non zero
            if(nums[i]!=0):
                nums[i],nums[count] = nums[count],nums[i]
                count+=1
        return nums

# creating object   
sol = Solution()

nums = [0,1,0,3,12]

sol.moveZeroes(nums)

print(nums)

            
            




        
