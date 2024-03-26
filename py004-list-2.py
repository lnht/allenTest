# x = [0] * 3
# y = [[0] * 3] * 3


# print(x)
# print(x[1] is x[0])
# print(y)
# print(y[0][0] is y[1][1])

# y[0][0] = 1
# print(y)


# str1 = "Hello"
# str2 = "Hello"
# str3 = str2
# print(str1 is str2)
# print(str2 is str3)

# str2 = "Hello..."
# print(str1 is str2)
# print(str2 is str3)
# print(str1 is str3)
# print(str3)

# a = [0, 0, 0]
# b = [0, 0, 0]
# print(a is b)


# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# for  i in matrix:
#     for j in i:
#         print(j)

matrix =[0]*3

for i in range(3):
    matrix[i] = [0]*3

print(matrix)

