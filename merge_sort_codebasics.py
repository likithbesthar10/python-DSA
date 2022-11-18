def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left_list = arr[:mid]
    right_list = arr[mid:]

    merge_sort(left_list)
    merge_sort(right_list)

    merge(left_list,right_list,arr)

def merge(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1
    
    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == "__main__":
    arr = [23,34,56,21,17,10,12,3,5,1] 
    merge_sort(arr)
    print(arr)       
