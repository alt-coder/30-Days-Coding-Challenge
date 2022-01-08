#https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
def slidingWindowMax(arr,k):
    deque=[0] #deque
    for i in range(1,k):
        while deque and arr[deque[-1]] <= arr[i]:
            deque.pop()
        deque.append(i)
    
    for i in range(k,len(arr)):
        print(arr[deque[0]], end= " ")
        
        while deque and deque[0] <= i-k:
            deque.pop(0)
        while deque and arr[deque[-1]] <= arr[i]:
            deque.pop()
        deque.append(i)
    print(deque[0],end="")

a="8 5 10 7 9 4 15 12 90 13"
arr = list(map(int,a.strip().split()))
slidingWindowMax(arr,4)
