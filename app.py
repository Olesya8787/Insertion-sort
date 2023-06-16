arr = [2, 1, 3, 5, 2]
arr_length = len(arr)
current_index = 1

while current_index < arr_length:
    current_element = arr[current_index]
    prev_i = current_index - 1
   
    while arr[prev_i] > current_element and prev_i >= 0:
        arr[prev_i + 1] = arr[prev_i]
        prev_i = prev_i - 1

    current_index += 1
    arr[prev_i + 1] = current_element

print(arr)        