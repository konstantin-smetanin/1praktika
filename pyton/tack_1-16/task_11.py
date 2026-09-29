def gu_by_se(ses):
    n=len(ses)
    result = [0] *n
    for k in range(n):
        gu_n=k+1
        se_in=ses[k]-1
        result[se_in]=gu_n
    return result
print(gu_by_se([1,2,3,5,4]))
print(gu_by_se([11,6,8,2,10,9,4,7,3,1,5]))
