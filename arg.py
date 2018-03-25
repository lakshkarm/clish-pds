import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
parser.add_argument("ip",type="int", help="give ip address of ctl")
parser.add_argument("nqn", type="str",help="give volume nqn ")
args = parser.parse_args()
for i in args:
    print i 
