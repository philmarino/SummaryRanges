def summaryRanges(nums):
    retArray = []
    tempArray = [nums[0], nums[0]]

    for num in nums:
        if num > tempArray[1] + 1:
            #start a new array
            retArray.append(tempArray)
            tempArray = [num, num]
        else:
            tempArray[1] = num
    retArray.append(tempArray)

    #now stringify the result
    retString = []
    for item in retArray:
        if item[0] == item[1]:
            retString.append(str(item[0]))
        else:
            retString.append(str(item[0]) + '->' + str(item[1]))
    
    return retString

# Example 1:
# Input: 
nums = [0,1,2,4,5,7]
print(summaryRanges(nums))
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

# Example 2:
# Input: 
nums = [0,2,3,4,6,8,9]
print(summaryRanges(nums))
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
 
