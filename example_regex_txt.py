import re
from pprint import pprint


interface_pattern = r'(.*Ethernet[1-9]/[0-9]*)'
native_vlan_pattern = r'.*native vlan\s([1-9][0-9]*)'

with open('interfaces.txt', 'r') as f:
    interfaces = f.read()
    interface_names = re.findall(interface_pattern,interfaces)
    interface_native_vlans = re.findall(native_vlan_pattern,interfaces)
    interface_dict = dict(zip(interface_names, interface_native_vlans))


#print(interfaces)
print(interface_names,end='\n\n')
print(interface_native_vlans,end='\n\n')
pprint (interface_dict)
