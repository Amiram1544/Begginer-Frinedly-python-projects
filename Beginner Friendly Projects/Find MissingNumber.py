#we want to code a program that get a list of numbers and find the missing number out of it from the min to max

#our list of numbers that we want to find the missing numbers out off it.
number = [-4, -1, 1, 2, 3, 5, 6, 7, 8, 22, 10, 18, 13, 14, 16, 20]


#define a func

def FindMissingNum(ListOfNum):
    nums = set(ListOfNum)
    b = max(nums)
    a = min(nums)
    output = []
    for numbers in range (a, b): #iterate over the list

        if numbers not in nums:
            output.append(numbers)
            
    return output

print( FindMissingNum(number))