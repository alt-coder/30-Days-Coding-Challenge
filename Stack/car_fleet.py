class Solution:
    '''
    logic is if a car at greater position takes more time than the car at lower position then all of them form a fleet
    '''
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        time=[] #store position and time of the array
        for i,j in zip(position,speed):
            time.append(((target-i)/j,i))
        time.sort(key = lambda x : x[1]) #sort the time according to position
        
        stack=[]
        for t,p in time:
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        return len(stack)