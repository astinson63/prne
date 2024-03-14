import getpass


def input_password():
    device_ip = input('Enter the device ip:')
    username = input('Enter the username:')
    password = getpass.getpass('Enter the password')
    
    print(f'Device IP: {device_ip}')



def input_int():
    vlan_id = input('\nPlease enter a vlan id (or don\'t for an exception):')
    
    try:
        vlan_id = int(vlan_id)
    except ValueError as e:
        print(f'\nValue Error Exception: Please enter a number for vlan id.\n\tException returned is: {e} \n')
    else:
        print('\nThanks for giving me a number!\n')
    finally:
        print('\nProcessing vlan...\n')

    try:
        print(f'VLAN ID is a number - I can add to it! Your vlan id: {vlan_id} + 10 = {vlan_id+10}')
    except TypeError as e:
        print(f'\nType Error Exception: VLAN ID is not type a number.\n\tException returned is: {e} \n')
    

#input_password()
input_int()
