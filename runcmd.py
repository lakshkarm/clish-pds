from subprocess import Popen, PIPE, STDOUT
import subprocess

cmd = 'ls'
'''
p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT,shell=True)
output = p.stdout.read()
print output
#print p.stdin.read()
#print p.stderr.read()
'''
#p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True )
p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
print p.stdout.read()
print p.stderr.read()
print p.stdin.read
