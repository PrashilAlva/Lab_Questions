lst=[]
while True:
    data=input('Enter the question or else press q to exit')
    if data=='q':
        break
    lst.append(data)

for ele in lst:
    if ele.endswith('?'):
        print(f'The question {ele} is Interrogative')
    else:
        print(f'The questions {ele} is Assertive')