from subprocess import Popen
import sys
import re
import logging

ip_pattern = '^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
logging.basicConfig(filename='ping.log', 
                    format=f'%(asctime)s \n%(levelname)s: %(message)s \n{"-"*80}',
                    datefmt='%x %X %Z',
                    level=logging.INFO)

def ping_host(ip='127.0.0.1'):
    count = 0
    while True:
        if count>10:
            logging.error(f'Ping to {ip} failed')
            sys.exit(f'Ping to {ip} failed.')
        # options are for linux based OS
        p = Popen(['ping',ip,'-c','1','-W','2'])
        logging.debug(p)
        p.wait()
        if p.poll() == 0:
            logging.info(f'Ping to {ip} succesful')
            print(f'Ping to {ip} succesful')
            break
        else:
            pass
        count += 1

def main():
    ip = input('Enter IP to Ping:')
    while not re.search(ip_pattern,ip):
        print('IP must be a real IP!')
        ip = input('Enter IP to Ping:')
    ping_host(ip)
        
if __name__ == '__main__': main()