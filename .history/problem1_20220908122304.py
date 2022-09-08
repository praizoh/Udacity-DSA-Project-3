def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number
    if type(number) is not int:
        try:
            if type(int(number)) is int:
                number = int(number)
            else:
                return -1
        except:
            return -1

    if type(int(number)) is not int:
        return -1

    start = 0
    end = number
    while start <= end:
        mid = (start + end) // 2
        if mid ** 2 == number:
            return mid
        elif mid ** 2 < number < (mid + 1) ** 2:
            return mid
        elif mid ** 2 > number:
            end = mid
        else:
            start = mid


print("Pass" if (3 == sqrt(9.0)) else "Fail")  # Pass
print("Pass" if (0 == sqrt(0)) else "Fail")  # Pass
print("Pass" if (4 == sqrt(16)) else "Fail")  # Pas
print("Pass" if (1 == sqrt(1)) else "Fail")  # Pass
print("Pass" if (5 == sqrt(27)) else "Fail")  # Pass
print("Pass" if (-1 == sqrt(None)) else "Fail")  # Pass
print("Pass" if (-1 == sqrt("")) else "Fail")  # Pass
print("Pass" if (-1 == sqrt("a")) else "Fail")  # Pass
