def sum_even_no(lst:list):
    def helper(l, r):
        if l == r:
            if l % 2 == 0 and lst[l] % 2 == 0:
                return lst[l]
            return 0
        mid = (l+r)//2
        return helper(l, mid) + helper(mid+1, r)
    return helper(0, len(lst)-1)
