print('===========================')
print('     Pizza Calculator')
print('==========================')
flavor = input('Enter pizza flavor(Hawaiian/Pepperoni/Cheese): ')

if flavor == 'Hawaiian':
    print('You selected Hawaiian Pizza')
    size = input('Enter size of Pizza (Small/Medium/Large/Jumbo):')
    if size == 'Small':
        price = 250
    elif size == 'Medium':
        price = 350
    elif size == 'Large':
        price = 500
    elif size == 'Jumbo':
        price = 1000
    else:
        price = 0
        print("Invalid Size")

elif flavor == 'Pepperoni':
    print('You selected Pepperoni Pizza')
    size = input('Enter size of Pizza (Small/Medium/Large/Jumbo):')
    if size == 'Small':
        price = 250
    elif size == 'Medium':
        price = 350
    elif size == 'Large':
        price = 500
    elif size == 'Jumbo':
        price = 1000

    else:
        price = 0
        print("Invalid Size")

elif flavor == 'Cheese':
    print('You selected Cheese Pizza')

    size = input('Enter size of Pizza (Small/Medium/Large/Jumbo): ')
    if size == 'Small':
        price = 250
    elif size == 'Medium':
        price = 350
    elif size == 'Large':
        price = 500
    elif size == 'Jumbo':
        price = 1000
    else:
        price = 0
        print("Invalid Size")

else:
    print("Invalid Pizza Flavor")

if price > 0:
    print("Pizza Price:", price)
else:
    print("Invalid Pizza Price")



