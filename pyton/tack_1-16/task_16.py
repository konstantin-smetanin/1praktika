def mon_cal(start_wek, d):
    cal_pust=["  "]* start_wek
    for day in range(1, d+1):
        cal_pust.append(f"{day:2}")
    weeks=[]
    for i in range(0,len(cal_pust),7):
        week_sl=cal_pust[i:i+7]
        week_str = " ".join(cal_pust)
        weeks.append(week_str.rstrip())
    return "\n".join(weeks)
if __name__ == "__main__":
    result = mon_cal(6,31)
    print(result)
    
