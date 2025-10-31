import sys

def inc_or_smash():
    numOfTests = int(input())
    # Process each test case
    for i in range(numOfTests):
        numOfElements = int(input())
         # Input elements for the array
        nums = []
        while len(nums) < numOfElements:
            nums += input().split()
        targetArray = list(map(int, nums[:numOfElements]))

        #print(targetArray)    
        # Find all the unique elements in the array, and save them to a set
        unique_elements = find_unique(targetArray)
        #print(unique_elements)

        len_unique = len(unique_elements)
        print(2*len_unique-1)

def find_unique(arr):
    unique_elements = set()
    for element in arr:
        unique_elements.add(element)
    return unique_elements

# def increase(arr, num):
#     for i in range(len(arr)):
#         arr[i] += num
#     return arr

# def smash(arr, num):
#     for i in range(num):
#         arr[i] = 0
#     return arr

#find min 

if __name__ == "__main__":
    inc_or_smash()