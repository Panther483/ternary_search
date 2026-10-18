def ternary_search(input_list, target):
    """This function divides the initial input list into 3 lists of roughly equal size
    and then determines which of the 3 lists could contain the desired value
    (assuming the original list is sorted) and if found uses its position in the
    sublist to return the position of the target in the original list or
    return None if it was not found."""

    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid1 = low + ((high - low) // 3)
        mid2 = high - ((high - low) // 3)
        if input_list[mid1] == target:
            return (mid1 + 1)
        if input_list[mid2] == target:
            return (mid2 + 1)

        if input_list[mid1] > target:
            high = mid1 - 1
        elif input_list[mid2] < target:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return None
#