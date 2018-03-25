import pexpect
import time
from pexpect import pxssh
import getpass
import random


class ClishCli:
    rl = [10,20,30,40,50,60,70,80,90,100]
    volsize = [100,200,250,300,150,350,400,500]
    vlist = []

    def __init__(self,hostname,username,password,ctl1,MediaGroup="manishmg1"):
        self.hostname   = hostname 
        self.username   = username 
        self.password   = password
        self.ctl1       = ctl1 
        self.MediaGroup = MediaGroup

    def sshClish(self):
        try:
            s = pxssh.pxssh()
            s.login(self.hostname, self.username, self.password)
            #s.sendline('uptime') 
            #s.prompt()
            #print(s.before)
            return s
        except pxssh.ExceptionPxssh as e:
            print("pxssh failed on login.")
            print (e)
        
    def psshObj(self):
        clishObj = self.sshClish()
        clishObj.sendline('su admin')
        clishObj.prompt()
        clishObj.sendline('switch config')
        clishObj.prompt()
        print(clishObj.before)
        return clishObj


## Assign a list of snapshot/clones to this methode to assign then to the controller port 
    def assignCopy(self,typ,copylist,port1,port2):
        clishObj = self.psshObj()
        for i in copylist:
            cmd = "assign copy type " +str(typ)+ " name" +str(i)+" port-id "+str(port1)+","+str(port2) 
            clishObj.sendline(cmd)
            clishObj.prompt()
        print(clishObj.before)
        clishObj.sendline('exit')
        clishObj.prompt()
        clishObj.sendline('exit')
        clishObj.prompt()
        clishObj.logout()


    def assignVol(self,vollist,port1,port2):
        clishObj = self.psshObj()
        for i in vollist:
            cmd = "assign volume name " + str(i)+ " port-id "+str(port1)+","+str(port2)
            clishObj.sendline(cmd)
            clishObj.prompt()
        print(clishObj.before)
        clishObj.sendline('exit')
        clishObj.prompt()
        clishObj.sendline('exit')
        clishObj.prompt()
        clishObj.logout()


    def unassignCopy(self,typ,copylist):
        clishObj = self.psshObj()
        for i in copylist:
            cmd = "unassign copy type "+str(type)+" name "+str(i)
            clishObj.sendline(cmd)
            clishObj.prompt()
        print(clishObj.before)

    def unassignVol(self,vollist):
        clishObj = self.psshObj()
        for i in vollist:
            cmd = "unassign volume name "+str(i)
            clishObj.sendline(cmd)
            clishObj.prompt()
        print(clishObj.before)

       

    def createVol(self,no,MediaG):
        clishObj = self.psshObj()
        vollist = []
        for i in range(no):
            res = random.choice(ClishCli.rl)
            size = random.choice(ClishCli.volsize)
            volname = "testmvol"+str(i)
            cmd = "create volume name "+str(volname)+" size "+str(size)+" GB grpname "+str(MediaG)+ " reserved "+str(res)
            clishObj.sendline(cmd)
            clishObj.prompt()
            vollist.append(volname)
        ClishCli.vlist = vollist
        print(clishObj.before)
        return vollist


    def createSnap(self,volname,no):
        snapList = []
        clishObj = self.psshObj()
        for i in range(no):
            cmd = "create copy type snapshot name "+str(volname)+"s"+str(i)+" parent-volume " + str(volname)
            clishObj.sendline(cmd)
            clishObj.prompt()
            snapList.append(volname+str(i))
            #time.sleep(5)
        print(clishObj.before)
        clishObj.sendline('exit')
        clishObj.sendline('exit')
        clishObj.prompt()
        print(clishObj.before)
        clishObj.logout()
        return snapList


    def createMg(self,mgname,zoneNo,mgtype):
        clishObj = self.psshObj()
        cmd = "create media-group name "+str(mgname)+" type "+str(mytype)+ " zone "+str(zoneNo)
        clishObj.sendline(cmd)
        clishObj.prompt()
        print(clishObj.before)
        clishObj.sendline('exit')
        clishObj.sendline('exit')
        clishObj.prompt()
        print(clishObj.before)
        clishObj.logout()

        
    
    def createClone(self,snapshot,no):
        #cloneResv = [10,20,30,40,50,60,70,80,90,100]
        cloneResv = [10,20,30]
        cloneList = []
        reservation = random.choice(cloneResv)
        clishObj = self.psshObj()
        for i in range(no):
            cmd = "create copy type clone name "+str(snapshot)+"c"+str(i)+" parent-snapshot " + str(snapshot) + " " + str(reservation)
            clishObj.sendline(cmd)
            clishObj.prompt()
            cloneList.append(snapshot+"c"+str(i))
        print(clishObj.before)
        clishObj.sendline('exit')
        clishObj.prompt()
        clishObj.sendline('exit')
        clishObj.prompt()
        clishObj.logout()
        return cloneList


    def deleteClone(self,cloneList=[]):
        clishObj = self.psshObj()
        print(clishObj.before)
        for i in cloneList:
            cmd = "delete copy name "+str(i)
            clishObj.sendline(cmd)
            clishObj.prompt()
        print(clishObj.before)
        clishObj.sendline('exit')
        clishObj.prompt()
        clishObj.sendline('exit')
        clishObj.prompt()
        clishObj.logout()

    
    def deleteSnap(self,L=[]):
        clishObj = self.psshObj()
        print(clishObj.before)
        for i in L:
            cmd = "delete copy name "+str(i)
            clishObj.sendline(cmd)
            time.sleep(3)
            clishObj.prompt()
            print(clishObj.before)
            time.sleep(30)
        print(clishObj.before)
        clishObj.sendline('exit')
        clishObj.prompt()
        clishObj.sendline('exit')
        clishObj.prompt()
        clishObj.logout()


    def deleteVol(self,list):
        clishObj = self.psshObj()
        print(clishObj.before)
        for i in list:
            cmd = "delete volume name "+str(i)
            clishObj.sendline(cmd)
            clishObj.prompt()
        print("Volumes deleted \n") 
        print(clishObj.before)
        clishObj.sendline('exit') 
        clishObj.sendline('exit') 
        clishObj.prompt()
        print(clishObj.before)
        clishObj.logout()


    
    def deleteMg(self):
        pass
        
     
        
if __name__=='__main__':
    obj = ClishCli("172.25.26.9","root","2bon2b","20")
    sshobj = obj.sshClish()
    sshobj.sendline('uptime')
    sshobj.prompt()
    print(sshobj.before)

# starting to create snapshots here 
    vollist = obj.createVol(1,"manishmg1")
    obj.assignVol(vollist,172,109)
    obj.unassignVol(vollist)
    obj.deleteVol(vollist)
    #obj.deleteSnap(snaplist)
    print "Task completed\n"




        
