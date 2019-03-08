#Heapify subtress rooted at index i
#Heapsize is n
def max_heapify(arr,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest]  = arr[largest], arr[i]
        max_heapify(arr,n,largest)

def build_max_heap(arr,n):
    for i in range(n//2-1,-1,-1):
        max_heapify(arr,n,i)

def heap_sort(arr):
    new_arr=[]
    n = len(arr)
    build_max_heap(arr,n)
    while n > 0:
        max = arr[0]
        arr[0],arr[n-1] = arr[n-1], arr[0]
        n = n - 1 
        max_heapify(arr,n,0)

def print_heap(A):
    print(A)


if __name__ == "__main__":
    A = [12,13,18,1,6,7,8,9,5,15]
    heap_sort(A)
    print_heap(A)