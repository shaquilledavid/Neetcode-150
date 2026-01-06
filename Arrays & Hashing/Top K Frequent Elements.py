def topKFrequent(nums, k):
    """Given an integer array nums and an integer k, return the k most frequent elements within the array.

    The test cases are generated such that the answer is always unique.

    You may return the output in any order.

    Example 1:

    Input: nums = [1,2,2,3,3,3], k = 2

    Output: [2,3]
    Example 2:

    Input: nums = [7,7], k = 1

    Output: [7]
    Constraints:

    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.
    """

    hashmap = {}

    for element in nums:
        if element not in hashmap:
            hashmap[element] = 1
        else:
            hashmap[element] += 1


    sorted_elements = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
    return list(sorted_elements.keys())[0:k]

nums = [1,2,2,3,3,3]
nums2=[1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
print(topKFrequent(nums2, k))
