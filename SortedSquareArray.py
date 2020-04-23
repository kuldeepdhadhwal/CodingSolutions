new_arr = [-5, -2, -1, 3, 4, 6, 7]

another_arr = [0, 0, 0, 0,0, 0, 0]

left = 0
right = len(another_arr) - 1

for i in range(right, -1, -1):
    if abs(new_arr[left]) < new_arr[right]:
        another_arr[i] = new_arr[right] *  new_arr[right]
        right -= 1
        print(right)
    
    else:
        another_arr[i] = new_arr[left] *  new_arr[left]
        left +=1
        

print(another_arr) 
