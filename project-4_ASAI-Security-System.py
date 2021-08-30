# users
Registered_Users = ['Murlidhar', "Sahil", 'ASAI', 'Skywalker', "Captain"]

# password
Admin_Password = "asaiinc"

while True:
    # self-intro
    print('\n Hello!  I\'m ASAI Security System :) ...')
    # username
    username = input('Enter Your User-ID\ Username: ').strip().capitalize()
    # verify user
    if username in Registered_Users:
        print(
            f"Welcome {username}, You Can Proceed Now... ").strip().capitalize()

        # ask to proceed further
        query1 = input(
            'Would you like to proceed further? (y/n); ').strip().lower()

        if query1 == 'y':
            # ask to be removed
            remove_user = input(
                'Would you want to be removed from the system? (y/n); ').strip().lower()
            if remove_user == 'y':

                # ask for the password
                verify_pass = int(input('Enter The Administrator Password; '))

                # remove user
                if verify_pass == password:
                    official_users.remove(user)

                else:
                    print('Sorry!  You\'ve Entered Wrong Password :( ')
                    continue

        else:
            continue

    # if user not in list
    else:
        print('Sorry!, I Didn\'t Recognized You :( \n')

        # ask to proceed further
        query2 = input(
            'Would you like to proceed further? (y/n); ').strip().lower()
        if query2 == 'y':

            # ask to be added
            update_user = input(
                'Would you want to be added to the system? (y/n); ').strip().lower()
            if update_user == 'y':

                # ask for the password
                verify_pass = int(input('Enter The Administrator Password; '))

                # update user
                if verify_pass == password:
                    official_users.append(user)

                else:
                    print('Sorry!  You\'ve Entered Wrong Password :( ')
                    continue

        else:
            continue
