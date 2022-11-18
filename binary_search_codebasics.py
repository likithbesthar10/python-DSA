def binary_search(numbers_list,number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

if __name__ == "__main__":
    numbers_list = [1,3,9,11,15,19,29]
    number_to_find1 = 25
    number_to_find2 = 15

    index1 = binary_search(numbers_list,number_to_find1)
    index2 = binary_search(numbers_list,number_to_find2)

    print(index1)
    print(index2)
                     