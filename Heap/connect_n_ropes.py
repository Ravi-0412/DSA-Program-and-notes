# for connecting n ropes with minimum cost
# you will have to pick the two smallest length always and connect them
# so min heap will work prefectly
# after connecting two ropes put them again into the heap 
# since there can be other combination possible with two smaller length
import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        if len(arr)==1:   # cost is zero
            return 0
        cost= 0
        heapq.heapify(arr)   # first make a min heap
        # now start taking the smaller two length and cal the cost
        while len(arr)>=2:  
            first= heapq.heappop(arr)  # pick the 1st smallest ele
            sec= heapq.heappop(arr)    # pick the 1st smallest ele
            curr_min= first+sec        # cost of conne the curr two rod of smaller length
            cost+= curr_min            # update the cost
            heapq.heappush(arr,curr_min)    # now push the cost of two picked one into heap 
                                            # as there can be other min possible with these picked one
        return cost




