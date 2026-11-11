nums=[5,9,7]
result=[]

def sub_seq_gen(ind, subset,result):
    if ind >= len(nums):
        #print(subset)
        result.append(subset.copy())
        return
    subset.append(nums[ind])
    sub_seq_gen(ind+1, subset, result)
    subset.pop()
    sub_seq_gen(ind+1, subset, result)

    


sub_seq_gen(0,[], result)
print(result)