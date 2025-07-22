import tabulate as tb

# initial warehouse data
warehouse = {
    '0001' : {'product' : 'Sensor',     'materialType' : 'Sparepart',   'stock' : 2,      'uom' : 'EA',   'location' : 'A1'},
    '0002' : {'product' : 'Glove',      'materialType' : 'Consummable', 'stock' : 360,    'uom' : 'PAA',  'location' : 'A3'},
    '0003' : {'product' : 'Motor',      'materialType' : 'Sparepart',   'stock' : 1,      'uom' : 'EA',   'location' : 'A1'},
    '0004' : {'product' : 'Gearbox',    'materialType' : 'Sparepart',   'stock' : 1,      'uom' : 'EA',   'location' : 'A2'},
    '0005' : {'product' : 'Mask',       'materialType' : 'Consummable', 'stock' : 50,     'uom' : 'BOX',  'location' : 'A4'}
}

# initial head for column
head = ['Material Code', 'Product', 'Material Type', 'Stock on Hand', 'UoM', 'Location']

# define & display table
def displayTable(data) :
    rows = []
    for key, info in data.items() :
        rows.append([key, info['product'], info['materialType'], info['stock'], info['uom'], info['location']])
    print()
    print(tb.tabulate(rows, headers=head, tablefmt='grid'))

# define menu
mainMenu = {
    1 : 'Show items in warehouse',
    2 : 'Update material',
    3 : 'Add new material',
    4 : 'Delete material',
    5 : 'Exit'
    }

submenu_items = {
    1 : 'Show all items',
    2 : 'Show selected items',
    0 : 'Back'
    }

submenu_search = {
    1 : 'Search by material code',
    2 : 'Search by material type',
    3 : 'Search by stock',
    4 : 'Search by location',
    0 : 'Back'
    }

submenu_update = {
    1 : 'Update stock',
    2 : 'Update location',
    0 : 'Back'
}

# main program
while True :
    print('\nWelcome to Warehouse Management System!')
    for key, val in mainMenu.items() :
        print(f'{key}. {val}')
    a = int(input('Please choose a menu: '))
    
    # menu read
    if a == 1 :
        while True :
            print('---------------------------------------------')
            print('\nHow do you want to show the data?')
            for key, val in submenu_items.items() :
                print(f'{key}. {val}')
            b = int(input('Choose an option: '))
            if b == 1 :
                print('---------------------------------------------')
                displayTable(warehouse)
                print('---------------------------------------------')
                cont = (input('\nDo you want to show another data? Y/N : ')).upper()
                if cont == 'Y' :
                    print('---------------------------------------------')
                    continue
                if cont == 'N' :
                    print('---------------------------------------------')
                    break
            elif b == 2 :
                print('---------------------------------------------')
                print('\nHow do you want to choose the data?')
                for key, val in submenu_search.items() :
                    print(f'{key}. {val}')
                c = int(input('Choose an option: '))
                if c == 1 :
                    while True :
                        print('---------------------------------------------')
                        code = input("\nEnter material code: ")
                        if code in warehouse :
                            print('---------------------------------------------')
                            displayTable({code: warehouse[code]})
                            print('---------------------------------------------')
                            cont1 = (input('\nDo you want to show another data? Y/N : ')).upper()
                            if cont1 == 'Y' :
                                continue
                            elif cont1 == 'N' :
                                break
                            else :
                                print('''Please choose only 'Y' or 'N'!''')
                        else :
                            print('---------------------------------------------')
                            print('\nMaterial not found!')
                            cont1 = input('\nDo you want to enter another material code? Y/N : ').upper()
                            if cont1 == 'Y' :
                                continue
                            elif cont1 == 'N' :
                                break
                            else :
                                print('''Please choose only 'Y' or 'N'!''')
                elif c == 2 :
                    while True :
                        print('---------------------------------------------')
                        materialType = input('\nEnter material type: ').capitalize()
                        results = {c:i for c,i in warehouse.items() if i['materialType'] == materialType}
                        if results :
                            print('---------------------------------------------')
                            displayTable(results)
                            print('---------------------------------------------')
                            cont1 = (input('\nDo you want to select another material type? Y/N : ')).upper()
                            if cont1 == 'Y' :
                                continue
                            elif cont1 == 'N' :
                                break
                            else :
                                print('''Please choose only 'Y' or 'N'!''')
                        else :
                            print('---------------------------------------------')
                            print('\nMaterial not found!')
                            cont1 = input('\nDo you want to continue? Y/N : ').upper()
                            if cont1 == 'Y' :
                                continue
                            elif cont1 == 'N' :
                                break
                            else :
                                print('''Please choose only 'Y' or 'N'!''')
                elif c == 3 :
                    while True :
                        print('---------------------------------------------')
                        stock = int(input('\nEnter stock value: '))
                        results = {c:i for c,i in warehouse.items() if i['stock'] == stock}
                        if results :
                            print('---------------------------------------------')
                            displayTable(results)
                            cont1 = (input('\nDo you want to search for another stock value? Y/N : ')).upper()
                            if cont1 == 'Y' :
                                continue
                            elif cont1 == 'N' :
                                break
                            else :
                                print('''Please choose only 'Y' or 'N'!''')
                        else :
                            print('---------------------------------------------')
                            print(f'\nNo items with stock {stock}!')
                            cont1 = input('\nDo you want to search for another stock value? Y/N : ').upper()
                            if cont1 == 'Y' :
                                continue
                            elif cont1 == 'N' :
                                break
                            else :
                                print('''Please choose only 'Y' or 'N'!''')
                elif c == 4 :
                    while True :
                        print('---------------------------------------------')
                        loc = input('\nEnter material location: ').upper()
                        results = {c:i for c,i in warehouse.items() if i['location'] == loc}
                        if results :
                            displayTable(results)
                            cont1 = (input('\nDo you want to search for another location? Y/N : ')).upper()
                            if cont1 == 'Y' :
                                continue
                            elif cont1 == 'N' :
                                break
                            else :
                                print('''Please choose only 'Y' or 'N'!''')
                        else :
                            print('\nPlease enter correct location!')
                elif c == 0 :
                    print('---------------------------------------------')
                    break
                else :
                    print('---------------------------------------------')
                    print('Invalid option! Please choose a correct option.')
            elif b == 0 :
                print('---------------------------------------------')
                break
            else :
                print('---------------------------------------------')
                print('Invalid option! Please choose a correct option.')

    # menu update                    
    elif a == 2 : 
        while True:
            print("\nWhich one will you update?")
            for key, desc in submenu_update.items():
                print(f"{key}. {desc}")
            u = int(input("Choose update type: "))
            if u == 1:
                print('---------------------------------------------')
                displayTable(warehouse)
                code = input("\nEnter material code to update stock: ")
                if code in warehouse:
                    print('---------------------------------------------')
                    new_stock = int(input("Enter new stock value: "))
                    warehouse[code]['stock'] = new_stock
                    print("\nStock updated.")
                    displayTable(warehouse)
                    print('\n---------------------------------------------')
                    cont1 = input('\nDo you want to update another material? Y/N : ').upper()
                    if cont1 == 'Y' :
                        continue
                    elif cont1 == 'N' :
                        break
                    else :
                        print('''Please choose only 'Y' or 'N'!''')
                else:
                    print('---------------------------------------------')
                    print("Material not found.")
            elif u == 2:
                print('---------------------------------------------')
                displayTable(warehouse)
                code = input("\nEnter material code to update location: ")
                if code in warehouse:
                    print('---------------------------------------------')
                    new_loc = input("Enter new location: ").upper()
                    warehouse[code]['location'] = new_loc
                    print("\nLocation updated.")
                    displayTable(warehouse)
                    cont1 = input('\nDo you want to update another material? Y/N : ').upper()
                    if cont1 == 'Y' :
                            continue
                    elif cont1 == 'N' :
                        break
                    else :
                        print('''Please choose only 'Y' or 'N'!''')
                else:
                    print('---------------------------------------------')
                    print("No material found!")
            elif u == 0:
                break
            else:
                print('---------------------------------------------')
                print("Invalid option! Please choose a correct option.")

    # menu create
    elif a == 3:
        while True :    
            print('\nPlease fill material informations below.')
            product = input("Enter product name: ").capitalize()
            mtype = input("Enter material type: ").capitalize()
            stock = int(input("Enter stock value: "))
            uom = input("Enter UoM: ").upper()
            loc = input("Enter location: ").upper()

            if warehouse:
                last = max(int(k) for k in warehouse.keys())
                new_code = str(last + 1).zfill(4)
            else:
                new_code = '0001'
            print('---------------------------------------------')
            print(f"\nAdding new material with code {new_code}.")

            warehouse[new_code] = {'product': product, 'materialType': mtype, 'stock': stock, 'uom': uom, 'location': loc}
            print('---------------------------------------------')
            print("\nMaterial added.")
            print('---------------------------------------------')
            displayTable(warehouse)
            print('\n---------------------------------------------')
            cont3 = input("\nDo you want to add more? Y/N : ").upper()
            if cont3 == 'Y' :
                continue
            elif cont3 == 'N' :
                break
    
    # menu delete
    elif a == 4 : 
        while True :
            displayTable(warehouse)
            code = input("\nEnter material code to delete: ")
            if code in warehouse:
                print('---------------------------------------------')
                confirm = input("Delete Material? (Y/N): ").upper()
                if confirm == 'Y' :
                    del warehouse[code]
                    print('---------------------------------------------')
                    print("\nMaterial deleted.")
                    displayTable(warehouse)
                    print('\n---------------------------------------------')
                    cont4 = input("\nDo you want to continue? Y/N : ").upper()
                    if cont4 == 'Y' :
                        continue
                    if cont4 == 'N' :
                        break
                elif confirm == 'N':
                    break
                else :
                    print('---------------------------------------------')
                    print("Invalid input.")
            else :
                print('---------------------------------------------')
                print("Material not found.")

    # menu exit
    elif a == 5 : 
        print("Exiting Program Warehouse Managament System.")
        print('---------------------------------------------')
        break

    else :
        print('---------------------------------------------')
        print("Menu not valid! Please enter a correct menu.")

            


            


