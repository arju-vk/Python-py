di={}
num = int(input("Enter the number of elements: "))
for i in range(num):
    value = input("Enter Value: ")
    di[i] = value
print((di))
for j in di:
    if j==1:
        print(di.keys())
        break



    