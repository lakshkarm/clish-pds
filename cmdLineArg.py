import argparse

argp = argparse.ArgumentParser(description='Trieal version on argparse')
argp.add_argument('-a',action='store',dest='ip_addr',help='store mgmt ip address')
argp.add_argument('-b',action='store',dest='USER',help='user')
argp.add_argument('-c',action='store',dest='PWD',help='password')
argp.add_argument('--version', action='version', version='%(prog)s 1.0')
result = argp.parse_args()

print result.ip_addr
print result
