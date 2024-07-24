import pandas as pd
import os


df=pd.read_excel("Downloads\sample.xlsx")
df1=df['Type']
list1= []
for i in df1:
    if "DSPR0" in str(i):
        i = "dspr0"
    if "DSPR_Core1" in str(i):
        i = "dspr1"
    if "DSPR_Core2" in str(i):
        i = "dspr2"
    if "LMURAM" in str(i):
        i = "lmuram"      
    if "PSPR_Core0" in str(i):
        i = "pspr0"
    if "PSPR_Core1" in str(i):
        i = "pspr1"
    if "PSPR_Core2" in str(i):
        i = "pspr2"
    if "PFlash0" in str(i):
        i = "pflash0"
    if "PFlash1" in str(i):
        i = "pflash1"
    list1.append(i)
df['Type'] = list1

df2=df.groupby('Type').sum().reset_index()
print(df2)
