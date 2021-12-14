def JobScheduling(Jobs,n):
    mp={}
    Jobs.sort(key= lambda x:x.profit,reverse=True)
    for job in Jobs:
        time= job.deadline
        if time not in mp:
            mp[time]=job.profit
        else:
            for i in reversed(range(1,time)):
                if i not in mp:
                    mp[i]=job.profit
                    break
    profit=0
    for k,v in mp.items():
        profit+=v
    return (len(mp.keys()),profit)