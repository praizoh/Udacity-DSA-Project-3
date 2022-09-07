def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0 or not all(isinstance(x, int) for x in input_list):
        return [-1]
    # sort the array in descending order
    def mergesort(items):
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]

        left = mergesort(left)
        right = mergesort(right)
        return merge(left, right)

    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(right[right_index])
                right_index += 1
            else:
                merged.append(left[left_index])
                left_index += 1

        merged += left[left_index:]
        merged += right[right_index:]
        return merged
    list_in_desc = mergesort(input_list)
    list_in_desc = list(map(str, list_in_desc))
    num_1 = list_in_desc[0::2]
    num_2 = list_in_desc[1::2]
    # merging the list into a single value

    return [int(''.join(num_1)), int(''.join(num_2))]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_case1 = [[""], [-1]]
test_function(test_case1)
test_case2 = [[], [-1]]
test_function(test_case2)
test_case3 = ["", [-1]]
test_function(test_case3)