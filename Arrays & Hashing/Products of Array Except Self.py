#Products of Array Except Self

def productExceptSelf(nums):
    """
    Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

    Each product is guaranteed to fit in a 32-bit integer.

    Follow-up: Could you solve it in 
    O(n) time without using the division operation?

    Example 1:

    Input: nums = [1,2,4,6]

    Output: [48,24,12,8]
    Example 2:

    Input: nums = [-1,0,1,2,3]

    Output: [0,-6,0,0,0]
    Constraints:

    2 <= nums.length <= 1000
    -20 <= nums[i] <= 20
    """

    output = []

    #prefix work
    prefix = 1
    prefix_arr = [1]

    i = 1
    while i < len(nums):
        prefix_arr.append(nums[i-1]*prefix)
        prefix *= nums[i-1]
        print("updated prefix =  " + str(prefix))
        i += 1


    #postfix work
    print("prefix arr =  " + str(prefix_arr))
    postfix = 1
    postfix_arr = [1]

    j = len(nums)-2
    while j >= 0:
        postfix_arr.append(postfix * nums[j+1])
        postfix *= nums[j+1]
        j -= 1

    #final output work

    postfix_arr.reverse()
    print("postfix arr =  " + str(postfix_arr))
    k = 0
    while k < len(nums):
        output.append(prefix_arr[k] * postfix_arr[k])
        k += 1

    return output

nums = [1,2,3,4]
print(productExceptSelf(nums))
