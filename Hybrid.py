print('===========================')
print('     Pizza Calculator')
print('==========================')
Laput_flavor = input('Enter pizza flavor(Fourcheese/ButterChicken/Overload): ').lower()

match Laput_flavor:
    case 'fourcheese' :
        print('You selected Fourcheese Pizza')
        Laput_size1 = input('Enter size of Pizza (Small/Medium/Large/Jumbo): ')
        match Laput_size1:
            case 'Small':
                price = 450
            case 'Medium':
                price = 500
            case 'Large':
                price = 750
            case 'Jumbo':
                price = 1000
            case _:
                price = 0
if Laput_flavor == 'butterchicken':
    print('butterChicken')
    size = input('Enter size of Pizza (Small/Medium/Large/Jumbo):')
    if size == 'Small':
        price = 450
    elif size == 'Medium':
        price = 500
    elif size == 'Large':
        price = 750
    elif size == 'Jumbo':
        price = 1000
    else:
        price = 0
        print("Invalid Size")

match Laput_flavor:
    case 'overload':
        print('You selected Overload Pizza')
        Laput_size = input('Enter size of Pizza (Small/Medium/Large/Jumbo):')
        match Laput_size:
            case 'Small':
                price = 450
            case 'Medium':
                price = 500
            case 'Large':
                price = 750
            case 'Jumbo':
                price = 1000
            case _:
                price = 0
                print("Invalid Size")

        print("Invalid Pizza Flavor")

if price > 0:
    print("Pizza Price:", price)
else:
    print("Invalid Pizza Price")