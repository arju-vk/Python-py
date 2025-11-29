# for i in range(1):
#     for j in range(3):
#         if j!=2:
#             print(j)
#             break
#         print(j)

# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j)
#     if i == 3:
#         break

# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j)
#     if i == 3:
#         break

n = int(input("Number : "))
lst = []
_sum = 0
for _ in range(n):
    x = int(input("NUM : "))
    lst.append(x)
    _sum += x
print(lst)
print(_sum)
