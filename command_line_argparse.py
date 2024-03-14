import argparse

text = 'This program takes input for router information'
parser = argparse.ArgumentParser(prog='My ArgParse Program',description=text)
#format : add_argument(short_option, long_option, help, action)
parser.add_argument('-R', '--router', help='Enter Router Name')
parser.add_argument('-IP', help='Enter IP Address')

router = parser.parse_args()

print(f'The router name is {router.router} with ip address {router.IP}')
