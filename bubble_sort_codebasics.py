def bubble_sort(numbers):
    size = len(numbers)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
                swapped = True
    
        if not swapped:
            break

if __name__ == "__main__":
    numbers = [1,67,98,34,76,34,23,12,67,89,46]
    bubble_sort(numbers)
    print(numbers)        

