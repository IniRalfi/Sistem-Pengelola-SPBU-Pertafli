def binary_search(sorted_data, key):
    low = 0
    high = len(sorted_data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if sorted_data[mid] == key:
            return mid
        elif sorted_data[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1