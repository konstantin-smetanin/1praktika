def is_div(a,b):
    if a==0:
        return False
    if b%a==0:
        return True
    else:
        return False
print(is_div(3,12))
print(is_div(5,12))
print(is_div(0,12))
print(is_div(7,0))
