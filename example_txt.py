border = '=================================================\n'
write_data = "router3 has an IP of 192.168.3.3 with a mask of 255.255.255.0"
writelines_data = ["router4 has an IP of 192.168.4.4 with a mask of 255.255.255.0",
                   "\n" "router5 has an IP of 192.168.5.5 with a mask of 255.255.255.0"
                   ]

def read_file():
    with open('example.txt', 'r') as f:
        print(f'{border}This is f.read: \n{f.read()}')

def readline_file():
    with open('example.txt', 'r') as f:
        print(f'{border}This is f.readline: \n{f.readline()}')
        
def readlines_file():
    with open('example.txt', 'r') as f:
        print(f'{border}This is f.readlines: \n{f.readlines()}')

def write_file():
    with open('example.txt', 'a') as f:
        f.write(write_data)
    read_file()

def writelines_file():
    with open('example.txt', 'a') as f:
        f.writelines(writelines_data)
    read_file()

def main():
    #read_file()
    #readline_file()
    #readlines_file()
    #write_file()
    writelines_file()

    print('\n')
    
if __name__ == '__main__': main()