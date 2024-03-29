from bs4 import BeautifulSoup

with open('example.xml', 'r') as f:
    xml_data = f.read()
    soup = BeautifulSoup(xml_data, features='xml')
    
print(f'\nDevice Type\tDevice Name\tIP\n{"-"*50}')
for router in soup.find_all('router'):
    print(f'Router\t\t{router["name"]}\t\t{router.ip.string}')
