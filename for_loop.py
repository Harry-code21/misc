#sum=0
#for i in range(0,11):
#    sum=sum+i

#print(sum)

n=int(input("enter a number"))
sum=0
for i in range(0,n+1,2):
    sum=sum+i
print(f"sum of even number from 0 to {n} is {sum}")