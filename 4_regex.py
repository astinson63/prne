#!/usr/bin/python3
import re

regex_data = {'GigabitEthernet2 ip address 192.168.1.0':
              ['address',
               'GigabitEthernet[1-4]',
               '[a-z][1-9]',
               '[A-Z][a-z]']}



def demo_pattern(re_pattern, re_data):
    print(f'Pattern:\t{pattern}')
    result = re.search(pattern,data)
    
    print(result)


for data in regex_data.keys():
    print(f'\n\nData:\t"{data}"\n')
    for pattern in regex_data[data]:
        demo_pattern(pattern, data)

