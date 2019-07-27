lower=int(input("Enter the lower bound?"))
upper=int(input("ENter the upper bound:"))


print(f"Prime nummbers between {lower} and {upper} are ",end='')
for i in range(lower,upper+1):
    flag=0
    for j in range(2,(i//2+1)):
        if i%j == 0:
            flag=1
            break
    if flag==0:
        print(f"{i},",end='')
