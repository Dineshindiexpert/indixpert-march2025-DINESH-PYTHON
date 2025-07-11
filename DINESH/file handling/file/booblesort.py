arr=[]
for i in range(10):
    element=int(input("enter your element :"))
    arr.append(element)
n = len(arr)

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if arr[j] > arr[j + 1]:
#              
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# print("Sorted array:", arr)



# assertion sorting 


n = len(arr)
arr=[1,3,4,5,5,7]
for i in range(1, n):
    key = arr[i]
    j = i - 1
    
     
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
        
    arr[j + 1] = key

print("Sorted array:", arr)
