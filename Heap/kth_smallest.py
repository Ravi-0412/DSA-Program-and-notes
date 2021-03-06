
# 1st method: selection sort 
# run the outer loop k times
# time: O(n^2)


# 2nd method: sort the elements and return the 'arr[k-1]'
# time: O(n^2)
arr=[1,3,5,7,9,2]
k=2
arr.sort()
print(arr[k-1])


# 3rd method: make a min heap and delete the k-1 element
# after that return the top ele of the array, that will be the kth smallest element


# third method: use max heap
import heapq
def KthSmallest(arr,k):
    heap= []
    for num in arr:
        heapq.heappush(heap,-num)
        if len(heap)> k:
            heapq.heappop(heap)
    return (-heap[0])

arr = [7,4,6,3,9,1]
print(KthSmallest(arr,3))

    



