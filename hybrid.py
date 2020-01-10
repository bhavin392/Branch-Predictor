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
readData=file.readline()
LHT=[0]*1024
LPT=[1]*1024
GHR=0
GPT=[1]*1024
misprediction=0
total=0


while readData:
    total+=1
    pc,data=readData.split(' ')
    pc=pc[-3:]
    if pc in LHT:
        pc1=pc[-2:]
        pc1=int(pc1)
        if 'T' in data or '1' in data:
            LPT[pc1]=LPT[pc1]+1
            GHR=GHR<<1
            GHR=GHR+1
            GHR=str(GHR)
            GHR=GHR[-1:]
            GHR = int(GHR)
            GHR=pc1^GHR
            GPT[GHR]=GPT[GHR]+1
            if GPT[GHR]<=0 or LPT[pc1]<=0:
                misprediction+=1
            if GPT[GHR]<=0:
                GPT[GHR]=0
                GPT[GHR]=0
            if LPT[pc1]<=0:
                LPT[pc1]=0
            if GPT[GHR]>=3:
                GPT[GHR]=3
            if LPT[pc1]>=3:
                LPT[pc1]=3
            

        if 'N' in data or '0' in data:
            LPT[pc1]=LPT[pc1]-1
            GHR=GHR<<1
            GHR=GHR+0
            GHR=str(GHR)
            GHR=GHR[-1:]
            GHR= int(GHR)
            GHR=pc1^GHR
            GPT[GHR]=GPT[GHR]+1
            if GPT[GHR]<=0 or LPT[pc1]<=0:
                misprediction+=1
                GPT[GHR]=0
                LPT[pc1]=0
            if GPT[GHR]>=3:
                GPT[GHR]=3
            if LPT[pc1]>=3:
                LPT[pc1]=3
            
            
    else:
        LHT.append(pc)
        if len(LHT)>=1024:
            del LHT[0]
            

        
                        
    
    readData=file.readline()

print("Misprediction:",misprediction)
print("Total Accesses:",total)
