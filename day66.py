num=input(print("enter number containing more than 1 digit"))
l=len(num)
sum=0
i=0
while i<l:
    sum=sum+int(num[i])
    i=i+1
    
print(sum)