num=int(input("Enter the number"))

sum=0

while True:
    if sum>=1 and sum<=9:
        break
    sum=0
    while True:
        if(num==0):
            break
        sum=sum+(num%10)
        num=num//10
    num=sum

print(f"Sum is:{sum}")