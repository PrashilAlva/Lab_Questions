dictio={}

def Add_product():
    idd=input('Enter the product id?')
    name=input('Enter the product name?')
    if idd in dictio:
        print('Item with same id already exist!')
    else:
        dictio[idd]=name

def display():
    if len(dictio) == 0:
        print('Dictionary is empty,No products entered')
    else:
        for ele in dictio:
            print(f"{ele}:{dictio[ele]}")

def search():
    idd=input('Enter the id to search?')
    if idd not in dictio:
        print('Product not found!')
    else:
        print('Product found!')
        print(f'Product ID:{idd} Product Name:{dictio[idd]}')

while True:
    print('*'*100)
    print('1.Add 2.Display 3.Search by name 4.Exit')
    print('*'*100)
    ch=int(input('Enter your choice?'))
    if ch==1:
        Add_product()
    elif ch==2:
        display()
    elif ch==3:
        search()
    else:
        break
