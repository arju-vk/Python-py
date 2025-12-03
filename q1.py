num=[1,2,3,1,1,3,2,3]
count=0
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]==num[j]):
            count+=1
print(count)