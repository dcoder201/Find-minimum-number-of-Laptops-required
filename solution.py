#User function Template for python3
import heapq
class Solution: 
    def minLaptops(self, N, start, end):
        # Code here
        ans = 0
        heap = []
        for s, e in sorted(zip(start, end)):
            while heap and heap[0] <= s:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
            ans = max(ans, len(heap))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input())
        start = list(map(int,input().split()))
        end = list(map(int,input().split()))
            
        ob = Solution()
        print(ob.minLaptops(N, start, end))
        
        T -= 1

# } Driver Code Ends
