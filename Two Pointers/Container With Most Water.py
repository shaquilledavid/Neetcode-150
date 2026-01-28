"""
You are given an integer array heights where heights[i] represents the height of the 
i'th bar

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4
"""
def maxArea(self, heights: List[int]) -> int:
    maxArea = 0
    i = 0
    j = len(heights) - 1
    while i < len(heights) - 1:
        print("i= "+str(i) + " j=" + str(j))
        smaller = min(heights[i], heights[j])
        #area is going to be the width x smaller
        area = (j - i)*smaller
        maxArea = max(maxArea, area)
        j -= 1
        if j == i:
            i += 1
            j = len(heights) - 1
                
        
    return maxArea
