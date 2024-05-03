#task1
def list1(lstp):
    res = 0
    for x in lstp:
        x += 1
        lstp[res] = x
        res += 1

    return lstp

print(list1([0,1,2,3]))
print(list1([2,4,6,8]))
print(list1([-1,-2,-3,-4]))



#task2
def list2(list1,list2):
    pass

print(list2([3,8],[1,5,95,0,4,7]))
print(list2([1,10],[1,10,25,8,11,6]))
print(list2([7,32],[1,2,3,78]))




#task3
print("'bu yerda siz tug'ilgan yilingizdan to xozirgacha bo'lgan kuningizni aniqlashingiz mumkun!")
def list3():
    inpa1 = int(input('yoshingiz: '))
    return f"siz {inpa1 * 365} kun yashadingiz!\n"
print(list3())



#task4
print("bu yerda son kiritasiz agar son listlarning elementini orasida bo'lsa true,bo'masa False")
def list4(list4):
    inpa4 = int(input('son: '))
    print(list4)
    if inpa4 in list4:
        return True
    return False

print(list4([0,1,2,3,4,5]))
print(list4([4,5]))
print(list4([6,7,8,9,10]))
print(list4([5]))



