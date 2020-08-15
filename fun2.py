num=int(input("enter a number to check even or odd : "))
def check(num):
    if num%2 == 0:
        return "even"
    else: 
        return "odd"

a=check(num)
print(f"{num} is {a}")

