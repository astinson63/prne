import re


def regex_ip_search():
    pattern = '\w+\s+([\d\.]+)\s.(YES)'
    data = "GigabitEtherent1  10.12.0.1  YES\nGigabitEthernet2  10.13.0.1  YES"
    
    result = re.search(pattern, data)
    
    print('*'.center(40,'*'),end='\n\n')
    print(f'pattern:\t{pattern}\ndata:\n{data}\n')
    print('*'.center(40,'*'),end='\n\n')
    print(f're.search object: {result}')
    print(f'Group 0: {result.group(0)}')
    print(f'Group 1: {result.group(1)}')
    print(f'Group 2: {result.group(2)}')

def regex_mac_search():
    data = 'internet 10.12.0.1 0050.56ac.ba7b\ninternet 10.12.0.1 0050.56ac.b87b\ninternet 10.12.0.1 0050.56ac.bd7b\ninternet 10.12.0.1 0050.56ac.bf7b\ninternet 10.12.0.1 0050.56ac.bg7b' 
    pattern = '((?:[0-9a-f]{4}\.){2}[0-9a-f]{4})'

    result = re.search(pattern, data,re.MULTILINE)
    
    print('*'.center(40,'*'),end='\n\n')
    print(f'pattern:\t{pattern}\ndata:\n{data}\n')
    print('*'.center(40,'*'),end='\n\n')
    print(f're.search object: {result}')
    print(f'Group 0: {result.group(0)}')
    print(f'Group 1: {result.group(1)}')
    print(f'result[1]: {result[1]}')

def regex_mac_findall():
    data = 'internet 10.12.0.1 0050.56ac.ba7b\ninternet 10.12.0.1 0050.56ac.b87b\ninternet 10.12.0.1 0050.56ac.bd7b\ninternet 10.12.0.1 0050.56ac.bf7b\ninternet 10.12.0.1 0050.56ac.bg7b' 
    pattern = '((?:[0-9a-f]{4}\.){2}[0-9a-f]{4})'

    result = re.findall(pattern, data,re.MULTILINE)
    
    print('*'.center(40,'*'),end='\n\n')
    print(f'pattern:\t{pattern}\ndata:\n{data}\n')
    print('*'.center(40,'*'),end='\n\n')
    print(f're.search object: {result}')
    for mac in result:
        print(f'mac found: {mac}')


def main():
    regex_ip_search()
    regex_mac_search()
    regex_mac_findall()
    
if __name__ == '__main__':main()
