from bs4 import BeautifulSoup

with open('example.xml', 'r') as f:
    xml_data = f.read()
    soup = BeautifulSoup(xml_data, features='xml')
    