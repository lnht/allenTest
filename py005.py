# import random

# M = []
# for i in range(88):
#     _m = []
#     for j in range(88):
#         _m.append(random(4))
        

#请使用列表推导式，创建一个内容为 [1, 4, 9, 16, 25, 36] 的列表？
# M = [(i+1)**2 for i in range(6)]
# print(M)

#请使用列表推导式，创建一个内容为 [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]] 
# M = [[i, i+2] for i in range(6)]
# print(M)

M = [1, 2, 3, 4, 5, 6]
del M[::2]
print( M)
