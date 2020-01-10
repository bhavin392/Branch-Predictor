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
pht = []
list1=[]
nbit=int(2)
nbit=pow(2,nbit)
nbitLength=int(nbit/2)
n=int(nbitLength/2)
print(nbitLength)

misprediction=0
goodprediction=0
for i in range(len(readData)):
    split= readData[i].split(' ')
    pc=split[0]
    pc=pc[-3:]
    data=split[1]
    if pc in list1:
        list1_index = list1.index(pc)
        if 'T' in data:
            pht[list1_index][0]=pht[list1_index][0]+1
            if pht[list1_index][0]>=nbit:
                pht[list1_index][0]=nbit
                
        if 'N' in data:
            pht[list1_index][0]=pht[list1_index][0]-1
            
            if pht[list1_index][0]<nbitLength-n:
                misprediction+=1
            if pht[list1_index][0]<=0:
                pht[list1_index][0]=0
    else:
        list1.append(pc)
        pht.insert(list1.index(pc),[1,pc])
        # misprediction+=1
        if len(pht)>1024:
            del pht[0]

print("Misprediction:",misprediction)
print("Total",len(readData))




    