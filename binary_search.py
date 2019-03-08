def binary_search(a,key):
    """Find the index of an element in the list"""
    low = 0 
    high = len(a)-1
    
    while low <= high:
        mid = low + (high - low) //2
        if a[mid] == key:
            return mid
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search1(a,key):
    """Find the index of first occurence of the key"""
    low = 0 
    high = len(a)-1
    ans = -1
    while low <= high:
        mid = low + (high - low) //2
        if a[mid] == key:
            ans = mid
            high = mid - 1
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return ans

def binary_search2(a,key):
    """Find the index of least element greater than the key """
    low = 0 
    high = len(a)-1
    ans = -1
    while low <= high:
        mid = low + (high - low) //2
        if a[mid] == key:
            low = mid + 1
        elif key < a[mid]:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def binary_search3(a,key):
    """Find the index of greatest element less than the key """
    low = 0 
    high = len(a)-1
    ans = -1
    while low <= high:
        mid = low + (high - low) //2
        if a[mid] == key:
            high = mid + 1
        elif key < a[mid]:
            high = mid - 1
        else:
            ans = mid
            #ans = mid if ans == -1 or a[mid] != a[ans] else ans   
            low = mid + 1
    return ans

def binary_search4(a,key):
    """Find the count of number of elements less than the key """
    low = 0 
    high = len(a)-1
    ans = -1
    while low <= high:
        mid = low + (high - low) //2
        if key < a[mid]:
            high = mid - 1
        else:
            ans = mid 
            low  = mid+1
    return ans+1

def binary_search5(a,key):
    """Find the count of number of elements greater or equal to  the key """
    low = 0 
    high = len(a)-1
    ans = -1
    while low <= high:
        mid = low + (high - low) //2
        if key <= a[mid]:
            ans = mid
            high = mid - 1
        else:
            low  = mid+1
    print(ans)
    return len(a)-ans if ans!=-1 else 0


def binary_search6(a,key):
    """Find the count of occurence of the number"""
    low = 0 
    high = len(a)-1
    start = -1
    while low <= high:
        mid = low + (high - low) //2
        if key == a[mid]:
            start = mid
            high = mid - 1
        elif key > a[mid]:
            low  = mid + 1
        else:
            high = mid - 1
    low = 0 
    high = len(a)-1
    end = -1
    while low <= high:
        mid = low + (high - low) //2
        if key == a[mid]:
            end = mid
            low = mid + 1
        elif key > a[mid]:
            low  = mid + 1
        else:
            high = mid - 1
    return end - start + 1 if end != -1 and start != -1 else 0

if __name__ == "__main__":
    a = [2,2,2, 4, 6, 11, 11, 11, 11, 12, 16, 18, 24, 25]
    a.sort()
    print(binary_search6(a,15))