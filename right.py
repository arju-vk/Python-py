# n = int(input("NUM :"))
# for i in range(1,n+1): 
#     for j in range(1,i+1):
#         print(j, end="")
#     print()  

# n=int(input("num :"))
# skip=int(input("num:"))
# x=1
# for i in range(n,0,-1):
#     if skip != x:
#         for j in range(1,i+1):
#             print(x,end="")
#         print()
#     x+=1

n=int(input("Num :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()