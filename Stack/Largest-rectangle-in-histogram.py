class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[]
        mxarea = 0
        for i,num in enumerate(heights):
            ix=i
            while stack and stack[-1][0] > num:
                height,idx = stack.pop()
                mxarea = max(mxarea, (i-idx)*height)
                ix=idx
            stack.append((num,ix))
        for height,idx in stack:
            mxarea= max(mxarea,(len(heights)-idx)*height)
        return mxarea