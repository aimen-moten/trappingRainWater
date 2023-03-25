# Leetcode 42: Trapping Rain Water

# Algorithm:
# First, you initialise two pointers, left and right at the start and end of the array respectively
# Then, you compute the maximum at left and right, which will initially just be the values at left and right
# You then have a while loop that executes when l < r
# Here, you shift the pointer based on which side has the lower value of the two maximums. This meas that if the leftMax is smaller, we do left++ else we do right--
# We then update the maxleft or maxright by taking the maximum of that value and the height we are currently at
# Finally, we add the area to a result variable. The area is computed by doing: maxleft-height[l] or maxright-height[r]
# In the end, we return the result.

# Code:

def trap(height: list[int]) -> int:
    l,r = 0, len(height)-1
    maxLeft, maxRight = height[l], height[r]
    res = 0
    while l < r:
        if maxLeft < maxRight:
            l += 1
            maxLeft = max(maxLeft, height[l])
            res += maxLeft - height[l]
        else:
            r -= 1
            maxRight = max(maxRight, height[r])
            res += maxRight - height[r]
    return res

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))