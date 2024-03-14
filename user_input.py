import getpass

def input_password():
    device_ip = input('Enter the device ip:')
    interfaces_to_return = 0
    
    try:
        interfaces_to_return = int(input('How many interfaces should I return?'))
    except TypeError as e:
        print(f'\nInvalid response - Please enter a number - Error:{e} \n')
    except ValueError as e:
        print(f'\nInvalid response - Please enter a number - Value Error:{e} \n')
    else:
        print('\nThanks for giving me a number!\n')
    finally:
        print('\nThis Try block has completed...\n')


    print(f'Device IP: {device_ip}')
    print(f'Interfaces to return: {interfaces_to_return}')


def input_int():
    value = input('Please enter a vlan:')
    try:        
        print(int(value)+10)
    except:
        print ('not an integer')
    print (f'Data type for value: {type(value)}')
    

input_password()
#input_int()
