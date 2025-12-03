Stuents_chocolates=[2,3,5,1,7]
additinal_chocolate = 3
max_Chocolate = max(Stuents_chocolates)
Final_result = {}
for i in Stuents_chocolates:
    if max_Chocolate <= i+additinal_chocolate:
        Final_result[i]=True
    else:
        Final_result[i]= False
print(Final_result)