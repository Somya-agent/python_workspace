def sub_seq_sum_k(list, k):
    length_list=len(list)
    start=len(list)
    end=len(list)
    i=0
    #print(f"length_list: {length_list}")

    for i in range(length_list):
        sub_list=[]
        sum=0
        start=i
        end=i
        #print(f"Outer {i} and {end}")
        while end < length_list:
            #print(f"Inner {i} and {end}")
            sum += list[end]
            if sum ==k:
                
                sub_list.append(list[end])
                print(sub_list)  
                if sum+list[end+1] > k :
                   break
                
                end+=1
            
            else:
                #sum += list[end]
                sub_list.append(list[end])
                end +=1
                
                

l=[1,4,0,3,2,1,0,3,0,5,0,4]
sub_seq_sum_k(l,5)
        