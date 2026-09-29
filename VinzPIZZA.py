print('===========================')
print('     Pizza Calculator')
print('==========================')
Laput_flavor = input('Enter pizza flavor(Fourcheese/ButterChicken/Overload): ').lower()

if Laput_flavor == 'Fourcheese' .lower():
    print('You selected Four_cheese Pizza')
    Laput_size1 = input('Enter size of Pizza (Small/Medium/Large/Jumbo):    ')
    if Laput_size1 == 'Small':
        price = 250
    elif Laput_size1 == 'Medium':
        price = 350
    elif Laput_size1 == 'Large':
        price = 500
    elif Laput_size1 == 'Jumbo':

        price = 1000
    else:
        price = 0
        print("Invalid Size")

elif Laput_flavor == 'ButterChicken':
    print('You selected ButterChicken Pizza')
    Laput_size2 = input('Enter size of Pizza (Small/Medium/Large/Jumbo):  ')
    if Laput_size2 == 'Small':
        price = 250
    elif Laput_size2 == 'Medium':
        price = 350
    elif Laput_size2 == 'Large':
        price = 500
    elif Laput_size2 == 'Jumbo':
        price = 1000

    else:
        price = 0
        print("Invalid Size")

elif  Laput_flavor == 'Overload' .lower():
    print('You selected Overload Pizza')
    Laput_size3 = input('Enter size of Pizza (Small/Medium/Large/Jumbo):   ')
    if  Laput_size3 == 'Small':
        price = 250
    elif Laput_size3 == 'Medium':
        price = 350
    elif Laput_size3 == 'Large':
        price = 500
    elif Laput_size3 == 'Jumbo':
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