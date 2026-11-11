#nums=[1,99,101,98,2,5,3,100,1,1,4,102,6]
nums=[1]

def sort():
    nums.sort()
    print(nums)
    print("------------")

sort()

def get_longest_sequence()-> int:
    i=0
    longest = -999
    prev_longest = 1
    prev_num = -999
    while i < len(nums):
        if(prev_num+1 == nums[i]):
            prev_longest += 1
            
            
        else:
            prev_longest=1

        if longest<prev_longest:
                longest = prev_longest
                

        prev_num = nums[i]
        i += 1
        

    return longest

result = get_longest_sequence()
print(f"Longest sequence : {result}")




