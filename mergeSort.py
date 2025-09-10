def merge_sort(arr):
    # base case
    if len(arr) <=  1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    results = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i])
            i+=1
        else:
            results.append(right[j])
            j+=1
    
    results.extend(left[i:])
    results.extend(right[j:])
    return results

arr = [8,3,5,2]
print(merge_sort(arr))


