def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i]['poin'] >= right[j]['poin']: 
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Tambahkan sisa elemen
    result.extend(left[i:])
    result.extend(right[j:])
    return result