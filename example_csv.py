import csv

write_data = [['device','ip','mask','admin'],
                ['router1','192.168.1.1','255.255.255.0',True],
                ['router2','192.168.2.2','255.255.255.0',False],
                ['router3','192.168.3.3','255.255.255.0',True],
                ['router4','192.168.4.4','255.255.255.0',False]
            ]


def read_file():
    print('Contents of example.csv:')
    with open('example.csv', 'r') as f:
        devices = csv.reader(f)
        header = next(devices)
        print(f'Headers: {header}')

        for row in devices:
            print(row)


def dictreader_file():
    with open('example.csv', 'r') as f:
        devices = csv.DictReader(f)

        for row in devices:
            print(row)


def write_file():
    print('Writing File:')
    with open('example2.csv', 'w') as f:
        devices = csv.writer(f)
        
        for row in write_data:
            devices.writerow(row)

    with open('example2.csv', 'r') as f:
        devices = csv.DictReader(f)

        for row in devices:
            print(row)
 
        
        
def main():
    print('\n')
    #read_file()
    #dictreader_file()
    write_file()

    print('\n')
    

if __name__ == '__main__': main()