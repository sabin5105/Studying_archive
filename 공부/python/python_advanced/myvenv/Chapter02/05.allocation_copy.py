# 리스트 할당 방식

# call by reference
x = [1,2,3,4,5]
y = x
print(x)
print(y)
print(id(x))
print(id(y))

# 얕은복사
y = x.copy()
y[2] = 0
print(x, y)
print(id(x))
print(id(y))

# 깊은복사 // 다차원 리스트 복사
import copy
x = [[1,2],[3,4,5]]
y = copy.deepcopy(x)
y[1][1] = 0
print(x ,y)
print(id(x))
print(id(y))

