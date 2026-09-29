def index_of_min(va):
    if not va:
        return -1
    mi_va =min(va)
    return va.index(mi_va)
print(index_of_min([10,-3,-5,2,5]))
print(index_of_min([1,2,3]))
print(index_of_min([4,1,1,9]))
print(index_of_min([]))
