import os
import time


def createFile(no,size,mnt):
    fileList = []
    for i in range(no):
        name = "mfile"+str(i)
        path = os.path.join(mnt,name)
        cmd = "fallocate -l "+str(size)+"M "+str(path)
        os.system(cmd)
        print "created ",path 
        fileList.append(name)
    return fileList


def deleteFile(mnt,filelist):
    for i in filelist:
        file = os.path.join(mnt,i)
        cmd = "rm -rf "+str(file)
        os.system(cmd)
        print "file deleted : ",file
    print "Files has deleted successfully\n"
    

def write():
    pass

filelist = createFile(2,2,"/test")
#print filelist
deleteFile("/test",filelist)



