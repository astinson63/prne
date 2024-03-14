import json
from pprint import pprint

json_data = [
    {
        'name': '1/0/1',
        'ip': '192.168.1.1',
        'mask': '255.255.255.0'
    }, {
        'name': '1/0/2',
        'ip': '192.168.2.2',
        'mask': '255.255.255.0'        
    }
]
python_dict = {'router1':{'ip':'192.168.1.1'}}


def read_file():
    print('Contents of example.json:')
    
    with open('example.json', 'r') as f:
        print(json.load(f))


def pprint_file():
    print('Contents of example.json:')
    
    with open('example.json', 'r') as f:
        pprint(json.load(f))

    

def write_file():
    print('Writing File example2.json...',end='')
    
    with open('example2.json', 'w') as f:
        json.dump(json_data, f, indent=2)

    with open('example2.json', 'r') as f:
        interfaces = json.load(f)
        
    print('done:')
    pprint(interfaces)


def main():
    print('\n')
    #read_file()
    #pprint_file()
    write_file()
    print('\n')
    

if __name__ == '__main__': main()