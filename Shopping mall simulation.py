print('Welcome to God is Good Mall...')

stock = {

        '101': {'name': 'bread', 'price': 500, 'qty': 100},

        '102': {'name': 'CD', 'price': 750, 'qty': 500},

        '103': {'name': 'Milo', 'price': 1500, 'qty': 100},

        '104': {'name': 'Milk', 'price': 1000, 'qty': 200},

        '105': {'name': 'Sardine', 'price': 550, 'qty': 500},

        '106': {'name': 'Honey', 'price': 1500, 'qty': 70},

        '107': {'name': 'Eggs', 'price': 2500, 'qty': 200},

        '108': {'name': 'Noodles', 'price': 3700, 'qty': 100},

        '109': {'name': 'Panadol Extra', 'price': 450, 'qty': 50},

        '110': {'name': 'Butter', 'price': 450, 'qty': 100}

    }

cart = {}

trial = 0

while trial < 3:

    choice = input('[0]: Show Stock\n[1]: Add to cart\n[2]: Edit Cart                \n[3]: Show Cart\n[4]: Checkout\n[#]: Exit\nEnter Option: ')



    if choice == '0':

        print(f'{"ID": <5}{"Name": <15}{"Price": >8}{"Qty": >5}')

        print('='*35)

        for key in stock:

            item = stock[key]

            print(f'{key: <5}{item["name"]: <15}{item["price"]: >8}{item["qty"]: >5}')

        print()

            

    elif choice == '1':

        key = input('Enter item id: ')

        if key in stock:

            if not key in cart:

                item = stock[key]

                qty = int(input('Enter qty: '))

                if qty > 0:

                    if item['qty'] >= qty:

                        cart[key] = {'name': item['name'], 'price': item['price'], 'qty': qty}

                    else:

                        print('out of stock') 

                else:

                    print('Invalid input')

            else:

                print('item already in cart\nchoose edit option')

        else:

            print('Invalid item id')

            trial += 1

    elif choice == '2':

        if cart:

            print(f'{"ID": <5}{"Name": <15}{"Price": >8}{"Qty": >5}')

            print('='*35)

            for key in cart:

                item = cart[key]

                print(f'{key: <5}{item["name"]: <15}{item["price"]: >8}{item["qty"]: >5}')

            print()

            

            item_id = input('Enter item id: ')

            if item_id in cart:

                new_qty = int(input('Enter new qty (to remove item, enter 0): '))

                if new_qty >= 0:

                    if new_qty == 0:

                        del cart[item_id]

                    elif new_qty <= stock[item_id]['qty']:

                        cart[item_id]['qty'] = new_qty

                        print('item updated...')

                    else:

                        print('out of stock')

                else:

                    print('Invalid input')

            else:

                print('Invalid item id')          

        else:

            print('Your cart is empty!!!')

    elif choice == '3':

        if cart:

            total = 0

            print(f'{"ID": <5}{"Name": <15}{"Price": >8}{" ":^3}{"Qty": >5}')

            print('='*50)

            for key in cart:

                item = cart[key]

                total += (item['price'] * item['qty'])

                print(f'{key: <5}{item["name"]: <15}{item["price"]: >8} {"*":^1}{item["qty"]: >5}{(item["price"] * item["qty"]): >10}')

            print('='*50)

            print(f'{total: >48}')

            print('='*50)

            print()

        else:

            print('Empty cart')

    elif choice == '4':

        if cart:

            total = 0

            print(f'{"ID": <5}{"Name": <15}{"Price": >8}{" ":^3}{"Qty": >5}')

            print('='*50)

            for key in cart:

                item = cart[key]

                total += (item['price'] * item['qty'])

                print(f'{key: <5}{item["name"]: <15}{item["price"]: >8} {"*":^1}{item["qty"]: >5}{(item["price"] * item["qty"]): >10}')

            print('='*50)

            print(f'{total: >48}')

            print('='*50)

            print()

            

            option = input('[1]: Proceed\n[2]: Cancel\n[#]: Previous Menu\n \
      Enter option: ')

            if option == '1':

                pymnt = float(input('Make payment: '))

                if pymnt >= total:

                    if pymnt > total:

                        balance = pymnt - total

                        print(f'Take your change: {balance}')

                    for key in cart:

                        if key in stock:

                            stock[key]['qty'] -= cart[key]['qty']

                    cart.clear()

                    print('Thanks for shopping')

                else:

                    print('Insufficient Fund')

                    continue

            elif option == '2':

                if input('Are you sure? Y/N').upper() == 'Y':

                    cart.clear()

                    print('Cart has been cleared')

            elif option == '#':

                continue

        else:

            print('Empty cart') 

        

    elif choice == '#':

        break

    else:

        print('Invalid option')

        trial += 1

    