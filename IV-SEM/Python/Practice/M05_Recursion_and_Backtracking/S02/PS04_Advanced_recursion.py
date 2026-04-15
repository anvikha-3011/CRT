#Digital root sum 
#386 --> 17 --> 8
def digital_root(n):
    if n <= 0:
        return 0
    s = sum([int(ch) for ch in str(n)])
    return digital_root(s) 

print(digital_sum(386)) 

#Sorted check 
def Sorted_Array(nums):
    pass 
print(Sorted_Array[10,20,30,40,50])
print(Sorted_Array[10,4,30,25,50])
