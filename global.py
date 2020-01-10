import tkinter as tk
from tkinter import filedialog
import numpy as np
import os
root= tk.Tk()
root.withdraw()
filepath =filedialog.askopenfilename(filetypes = (("trace files","*.trace"),("out files",".out")))
file=open(filepath)
file_path = file.name
ext= os.path.splitext(file_path)
readData=file.readlines()
nbit=int(2)
nbit=pow(2,nbit)
nbitLength=int(nbit/2)
n=int(nbitLength/2)
print(nbitLength)
pht = []
list1=[]
gtr=0
misprediction=0
goodprediction=0
for i in range(len(readData)):
    split= readData[i].split(' ')
    data=split[1]
    if gtr in list1:
        list1_index = list1.index(gtr)
        if 'T' in data:
            gtr=gtr&0xffffffffff
            gtr=gtr<<1
            gtr=gtr+1
            gtr=gtr&0xffffffffff
            gtr=gtr&0x0000003ff0
            gtr=gtr>>4
            pht[list1_index][0]=pht[list1_index][0]+1
            if pht[list1_index][0]>=nbit:
                pht[list1_index][0]=nbit
            
        if 'N' in data:
            gtr=gtr&0xffffffffff
            gtr=gtr<<1
            gtr=gtr+0
            gtr=gtr&0xffffffffff
            gtr=gtr&0x0000003ff0
            gtr=gtr>>4
            pht[list1_index][0]=pht[list1_index][0]-1
            if pht[list1_index][0]<nbitLength-n:
                misprediction+=1
            if pht[list1_index][0]<=0:
                pht[list1_index][0]=0

    else:
        list1.append(gtr)
        misprediction+=1
        pht.insert(list1.index(gtr),[1,gtr])
        if len(pht)>1024:
            del pht[0]

print("Misprediction:",misprediction)
print("Total",len(readData))