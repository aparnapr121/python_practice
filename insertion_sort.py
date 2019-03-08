def insertion_sort(a):
    for j in range(1,len(a)):
        key = a[j]
        i = binary_search(a,key,0,j-1)
        a = a[:i]+[key]+a[i:j]+a[j+1:]
    return a


def binary_search(input_list,item,low,high):
    if low == high:
        return low if input_list[low] > item else low+1
    if low > high:
        return low

    mid = (low + high) // 2
    if item == input_list[mid]:
        return mid 
    elif item < input_list[mid]:
        high = mid - 1
    else:
        low = mid + 1
    return binary_search(input_list, item, low, high)

if __name__ == "__main__":
    print("Enter the input list")
    user_list = list(map(int,input()))
    print("sorted list")
    print(insertion_sort(user_list))



