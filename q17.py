lst=[]
while True:
    data=input('Enter the Singular word or else press q to exit')
    if data=='q':
        break
    lst.append(data)

for ele in lst:
    str=''
    for data in ele:
        if data=='y':
            str=str+'ies'
        else:
            str=str+data
    print(f'The Plural of {ele} is {str}')



