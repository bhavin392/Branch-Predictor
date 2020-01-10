import tkinter as tk
from tkinter import filedialog
import numpy as np
import sys
import os
root= tk.Tk()
root.withdraw()
filepath =filedialog.askopenfilename(filetypes = (("trace files","*.trace"),("out files",".out")))
file=open(filepath)
file_path = file.name
ext= os.path.splitext(file_path)
readData=file.readlines()
pht=[]
local=[0]*128
list1=[]
nbit=int(sys.argv[1])
nbit=pow(2,nbit)
nbitLength=int(nbit/2)
n=int(nbitLength/2)
print(nbitLength)
addr=0
addr1=0
misprediction=0

for i in range(len(readData)):
    split= readData[i].split(' ')
    pc=split[0]
    pc=int(pc)
    pc=pc&0x000007f0
    pc=pc>>4
    data=split[1]
    addr1=local[pc]
    addr1=addr1&0xffffffffff
    addr=addr<<1
    if addr in list1:
        list1_index = list1.index(addr)
        if 'T' in data or '1' in data:
            local[pc]=addr
            addr=local[pc]&0x00003ff0
            addr=addr>>4
            pht[list1_index][0]=pht[list1_index][0]+1
            if pht[list1_index][0]>=nbit:
                pht[list1_index][0]=nbit
        
        if 'N' in data or '1' in data:
            local[pc]=pht[list1_index][1]
            addr=local[pc]&0x00003ff0
            addr=addr>>4
            pht[list1_index][0]=pht[list1_index][0]-1
            if pht[list1_index][0]<nbitLength-n:
                misprediction+=1
            if pht[list1_index][0]<=0:
                pht[list1_index][0]=0
           
                
    else:
        list1.append(addr)
        pht.insert(list1.index(addr),[1,addr])
        if len(pht)>1024:
            del pht[0]
print("Misprediction:",misprediction)
print("Total",len(readData))
                

