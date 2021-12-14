class Solution:
    def __init__(self) -> None:
        pass
        
    def minc(self, coins, M, V, mp):
        if (M,V) in mp:
            return mp[(M,V)]
        elif V==0:
            mp[(M,V)] = 0
        elif V < 0 or (M <= 0) or len(coins) == 0:
            mp[(M,V)] = 999999
        elif coins[0] > V:
            mp[(M,V)] = self.minc(coins[1:],M-1,V,mp)

        else:
            num=0
            Vt=V
            while Vt >= coins[0]:
                num+=1
                Vt-=coins[0]
            mp[(M,V)] = min(num+self.minc(coins[1:],M-1,Vt,mp),self.minc(coins[1:],M-1,V,mp))
        return mp[(M,V)]
    def minCoins(self, coins, M, V):
        # code here
        coins.sort(reverse=True)
        mp={}
        ad=self.minc(coins, M, V, mp)
        
        return mp[(M,V)] if mp[(M,V)] < 999999 else -1

ob = Solution()
print(ob.minCoins([3,7,6,11,8],5,26))