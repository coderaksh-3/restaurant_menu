#  || ----- HOTEL PROJECT ----- ||

print('||                WELCOME TO HOTEL - SHIVRAI !                ||')


rlist = []
class Restaurant:
    def __init__(s, name='', email='', contact=0, password='', confirm_password='', veg_price=0, nonveg_price=0, total_bill=0):
        s.name = name
        s.email = email
        s.contact = contact
        s.password = password
        s.confirm_password = confirm_password
        s.veg_price = veg_price
        s.nonveg_price = nonveg_price
        s.total_bill = total_bill


    def __str__(s):
        return s.name + '\t' + s.email + '\t' + str(s.contact) + '\t' + s.password + '\t' + s.confirm_password +'\t'+ str(s.veg_price) +'\t'+ str(s.nonveg_price) +'\t'+ str(s.total_bill)
    

    def register(s):
        print('Register to Continue'.center(60,' '))
        print('='*60)
            
        s.name = input('Name : ')
        s.email = input('E-mail ID : ')
        s.contact = int(input('Contact : '))
        s.password = input('Password : ')
        s.confirm_password = input('Confirm Password : ')
        if s.password == s.confirm_password:
            r = Restaurant(s.name, s.email, s.contact, s.password, s.confirm_password)
            rlist.append(r)
            print('Registration Successful!'.center(60,' '))
        else:
            print("Password Doesn't Match - Please Register Again...".center(60,' '))


    def login(s):
        print('Login to Continue'.center(60,' '))
        print('='*60)
        id_co = input('Registered E-mail ID or Contact : ')
        pwd = input('Registered Password : ')
        for i in rlist:
            if (id_co == i.email or pwd == i.password) and (id_co == i.contact or pwd == i.password):
                print('-'*60)
                print(f'Welcome {i.name}, Please Explore your Choices !'.center(60,' '))
                print('-'*60)
                s.order()

                print('Login Details'.center(20,' '))
                print('-'*60)
                print('Name : ', s.name)
                print('E-mail ID : ', s.email)
                print('Contact : ', s.contact)
                print('-'*60)
                
            else:
                print('Please enter valid E-mail and Password...'.center(60,' '))
                print('-'*60)
                    

                    

    def veg_menu(s):
        print("Hungry! Grab Your Food!".center(60,' '))
        print('-'*60)
        print('                     VEG MENU                    ')
        print('-'*60)
        print('Sr.No:          Menu                     Price   ')
        print('='*60)
        print('  1.       Veg. Paneer Makhni            Rs.190  ')
        print('  2.       veg. Manchurian               Rs.250  ')
        print('  3.       Veg. Dum Biryani              Rs.350  ')
        print('  4.       Masala Dosa                   Rs.180  ')
        print('  5.       Cheese Pav Bhaji              Rs.210  ')
        print('-'*60)
        print('                                                 ')

        order = int(input('Select your order by Sr.No : '))
        qty = int(input('Quantity : '))
        print('-'*60)

        if order == 1:
            s.veg_price = 190*qty
            print('Veg. Paneer Makhni = Rs. ', s.veg_price)

        elif order == 2:
            s.veg_price = 250*qty
            print('Veg. Manchurian = Rs. ', s.veg_price)

        elif order == 3:
            s. veg_price = 350*qty
            print('Veg. Dum Biryani = Rs. ', s.veg_price)

        elif order == 4:
            s.veg_price = 180*qty
            print('Masala Dosa = Rs. ', s.veg_price)

        elif order == 5:
            s.veg_price = 210*qty
            print('Cheese Pav Bhaji = Rs. ', s.veg_price)
            
        else:
            print('Please select from above Menu List...')

        print('Your Current Bill Amount = Rs. ', s.veg_price)
        print('-'*60)
        for i in rlist:
            i.veg_price += s.veg_price


    def nonveg_menu(s):
        print("Hungry! Grab Your Food!".center(60,' '))
        print('-'*60)
        print('                   NON-VEG MENU                  ')
        print('-'*60)
        print('Sr.No:          Menu                     Price   ')
        print('='*60)
        print('  1.       Butter Chicken                Rs.250  ')
        print('  2.       Mutton Biryani                Rs.540  ')
        print('  3.       Promphet Fry                  Rs.450  ')
        print('  4.       Tandoori Chicken              Rs.340  ')
        print('  5.       Chicken Biryani               Rs.280  ')
        print('-'*60)

        order = int(input('Select your order by Sr.No : '))
        qty = int(input('Quantity : '))
        print('-'*60)

        if order == 1:
            s.nonveg_price = 250*qty
            print('Butter Chicken = Rs. ', s.nonveg_price)

        elif order == 2:
            s.nonveg_price = 540*qty
            print('Mutton Biryani = Rs. ', s.nonveg_price)

        elif order == 3:
            s.nonveg_price = 450*qty
            print('Promphet Fry = Rs. ', s.nonveg_price)

        elif order == 4:
            s.nonveg_price = 340*qty
            print('Tandoori Chicken = Rs. ', s.nonveg_price)

        elif order == 5:
            s.nonveg_price = 280*qty
            print('Chicken Biryani = Rs. ', s.nonveg_price)

        else:
            print('Please select from above Menu List...')
                                
        print('Your Current Bill Amount = Rs. ', s.nonveg_price)
        print('-'*60)
        for i in rlist:
            i.nonveg_price += s.nonveg_price
        

    def check_details(s):
        print('CUSTOMER LOGIN DETAILS'.center(60,'-'))
        for i in rlist:
            print('Name : ',i.name)
            print('E-mail ID : ', i.email)
            print('Contact : ', i.contact)
        print('-'*60)


    def update_details(s):
        print('NAME E-MAIL CONTACT'.center(60,'-'))
        id_co = input('E-mail ID : ')
        for i in rlist:
            if id_co == i.email:
                i.name = input('Name : ')
                i.contact = int(input('Contact : '))
                i.password = input('Password : ')
                i.confirm_password = input('Confirm Password : ')
                print('-'*60)
                print('Details Updated Succesfully'.center(60,' '))
        print('-'*60)


    def delete(s):
        id_co = input('Registered E-mail ID : ')
        for i in rlist:
            if id_co == i.email:
                code = input('Enter D to Delete Account Permanently : ')
                if code.upper() == 'D':
                    rlist.remove(i)
                    print('-'*60)
                    print('Account Deleted Permanently'.center(60,' '))
                    print('-'*60)
                else:
                    print('Sorry! Please Try Again'.center(60,' '))


    def bill(s):
        print('='*60)
        print('HOTEL SHIVRAI BILL'.center(60, ' '))
        print('_'*60)
        print('Customer Details'.center(60, ' '))
        print('-'*60)
        print('Name : ', s.name)
        print('E-mail ID : ', s.email)
        print('Contact : ', s.contact)
        print('-'*60)
        
        for i in rlist:
            i.total_bill = i.veg_price + i.nonveg_price
            print("Veg Bill :            Rs. ", i.veg_price)
            print(' '*60)
            print("Non-Veg Bill :        Rs. ", i.nonveg_price)
            print('='*60)
            print("Total Bill Amount :   Rs. ", i.total_bill)
            print('-'*60)


    def order(s):
        choice = 1
        while choice != 0:
            try:
                print('Enter 1 - Veg Order')
                print('Enter 2 - Non-Veg Order')
                print('Enter 3 - Check User Details')
                print('Enter 4 - Update User Details')
                print('Enter 5 - Delete Account')
                print('Enter 6 - Check Total Bill Amount')
                print('Enter 0 - Exit')
                print('-'*60)
                choice = int(input('Select : '))

            except:
                print('Invalid Choice')
                break
            
            if choice==1:
                 s.veg_menu()
                 
            elif choice==2:
                 s.nonveg_menu()
                 
            elif choice==3:
                 s.check_details()
                 
            elif choice==4:
                 s.update_details()
                 
            elif choice==5:
                 s.delete()
                 
            elif choice==6:
                 s.bill()

            else:
                print('Please Login Again!'.center(60,' '))

            


def booking_status():
    r = Restaurant()
    choice = 1
    
    while choice != 0:
        try:
            print('-'*60)
            print('Enter 1 - Register')
            print('Enter 2 - Login')
            print('Enter 0 - Exit')
            print('-'*60)
            choice = int(input('Select : '))

        except:
            print('Invalid Choice')
            break
            
        if choice == 1:
            r.register()
            
        elif choice == 2:
            r.login()

        else:
            print('Do Check-out Our Services!'.center(60,' '))

        


booking_status()
