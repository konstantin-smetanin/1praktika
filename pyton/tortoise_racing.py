def race(v1, v2, g):
    if v1 >=v2:
        return False
    v1_sekond=v1/3600
    v2_sekond=v2/3600
    a=g
    b=0 #позиции черепах
    sekund=0
    while b<a:
        a+=v1_sekond 
        b+=v2_sekond
        sekund+=1 #движение каждую секунду пока а впереди
    h=sekund//3600
    m=(sekund % 3600) //60
    s=sekund %60 -1 #перевод в часы минуты секунды
    return [h,m,s]
print(race(720, 850, 70))   # [0, 32, 18]
print(race(820, 81, 550))    # None
print(race(80, 91, 37))      # [3, 21, 49]
print(race(80, 100, 40))     # [2, 0, 0]
print(race(720, 850, 370))   # [2, 50, 46]
print(race(820, 850, 550))   # [18, 20, 0]
print(race(100, 100, 50))   #None
    
