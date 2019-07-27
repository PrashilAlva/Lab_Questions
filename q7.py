lb=int(input('Enter the lower bound:'))
ub=int(input('Enter the upper bound:'))
for ele in range(lb,ub+1):
    if ele%9==0 and not(ele%5==0):
        print(f"{ele}",end=' ')