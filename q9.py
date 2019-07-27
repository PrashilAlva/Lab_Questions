num=int(input("Enter the no?"))
count=0
while True:
    if num==0:
        break
    temp=num%10
    num=num//10
    flag=0
    if temp == 1:
        continue
    else: 
        for j in range(2,(temp//2+1)):
            if temp%j == 0:
                flag=1
        if flag==0:
            count=count+1

print(f"The total Prime number in {num} is {count}")
