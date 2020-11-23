from itertools import starmap

def poisk(*nums):
    return max(nums)**2

def maximize(lists, m):
    try:
        ans=0
        for el in starmap(poisk,lists):
            ans+=el
        return ans%m

    except:
        raise RuntimeError("Not implemented")
