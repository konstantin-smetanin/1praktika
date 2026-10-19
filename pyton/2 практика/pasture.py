def pasture_area (wire, w):
    if w<=0 or w*2 >wire:
        return 0
    l= (wire - 2*w)/3
    return w*l
def best_pasture(wire):
    w=wire/4
    l=(wire -2* w)/3
    area=w*l
    return (w,l,area)
print(pasture_area(100, 25))     # 416.666...
print(pasture_area(100, 10))     # 266.666...
print(pasture_area(100, 50))     # 0.0    вся проволока ушла на ширину

print(best_pasture(100))         # (25.0, 16.666..., 416.666...)
print(best_pasture(60))          # (15.0, 10.0, 150.0)
print(best_pasture(12))          # (3.0, 2.0, 6.0)    
