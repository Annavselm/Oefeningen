def hello(naam):
    res = ("welcome, " + naam + ", to the world of python")
    return res

print (hello("Anna"))

def rng(listofnumbers):
    res = max(listofnumbers) - min(listofnumbers)
    return res

print(rng([5, -6, 13, 10, -3, -14]))

def swapFS(lst):
    if len(lst) > 1:
        lst[0], lst[1] = lst[1], lst[0]
