def biggest(my_list):
    sum=0
    for ele in my_list:
        sum=sum+ele
    return sum

liste=[]
while True:
    data=input("Enter the element or press q to exit")
    if data=='q':
        break
    liste.append(int(data))
sum=biggest(liste)
print(f"Sum of list is {sum}")