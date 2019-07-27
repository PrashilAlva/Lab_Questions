num=int(input("Enter the number?"))
fact=1
while True:
    if num==0:
        break
    fact=fact*num
    num=num-1

print(f"Factorial is:{fact}")