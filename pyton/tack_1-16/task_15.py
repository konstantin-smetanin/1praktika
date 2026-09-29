def day_in_mon(month,year):
    is_v=(year %4==0 and year %100!=0)or(year %400==0)
    day_per_mounth=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if month==2 and is_v:
        return 29
    return day_per_mounth[month]
print(day_in_mon(1,2001))
print(day_in_mon(2,2001))
print(day_in_mon(2,2000))
print(day_in_mon(2,1900))
print(day_in_mon(11,2025))
