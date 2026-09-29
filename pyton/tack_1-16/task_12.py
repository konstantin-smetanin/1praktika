def sh_dis(km,m):
    km_in_m=km*1000
    if km_in_m<m:
        return km_in_m
    else:
        return m
print(sh_dis(1,500))
print(sh_dis(0.2,900))
print(sh_dis(1,1000))
